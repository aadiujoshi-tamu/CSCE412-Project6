"""Coordinates specialized agents without letting AI mutate infrastructure."""
from __future__ import annotations
from .base import Feedback, Result, Task
class Orchestrator:
    def __init__(self, agents): self.agents = {a.role: a for a in agents}
    def dispatch(self, task: Task) -> Result:
        if task.role not in self.agents: return Result(task_id=task.id, role="orchestrator", status="failed", summary="No agent assigned for role.")
        return Result.model_validate(self.agents[task.role].run(task.model_dump()))
    def feedback(self, result: Result, accepted: bool, note: str) -> Feedback:
        return Feedback(task_id=result.task_id, accepted=accepted, note=note)
