"""Shared schemas and safe, provider-agnostic agent execution."""
from __future__ import annotations
import json
from collections.abc import Callable
from typing import Any, Literal
from pydantic import BaseModel, Field, ValidationError

class Task(BaseModel):
    id: str
    role: str
    objective: str
    evidence: dict[str, Any] = Field(default_factory=dict)

class Feedback(BaseModel):
    task_id: str
    accepted: bool
    note: str

class Result(BaseModel):
    task_id: str
    role: str
    status: Literal["ok", "needs_approval", "failed"]
    summary: str
    evidence: dict[str, Any] = Field(default_factory=dict)
    proposed_action: str | None = None

Tool = Callable[[dict[str, Any]], dict[str, Any]]

class EvidenceAgent:
    """Runs validated local tools; malformed LLM output falls back to evidence."""
    role = "base"
    def __init__(self, tools: dict[str, Tool] | None = None): self.tools = tools or {}
    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in self.tools: return {"error": f"tool not allowed: {name}"}
        try:
            output = self.tools[name](arguments)
            return output if isinstance(output, dict) else {"error": "invalid tool output"}
        except Exception as exc: return {"error": str(exc)}
    def analyze(self, task: Task) -> Result: raise NotImplementedError
    def run(self, raw_task: dict[str, Any]) -> dict[str, Any]:
        try: return self.analyze(Task.model_validate(raw_task)).model_dump()
        except (ValidationError, ValueError) as exc:
            return Result(task_id=raw_task.get("id", "unknown"), role=self.role, status="failed", summary="Agent input was invalid; preserved raw evidence.", evidence={"error": str(exc), "raw": raw_task}).model_dump()

def load_json(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as source: return json.load(source)
