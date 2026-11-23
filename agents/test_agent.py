from .base import EvidenceAgent, Result, Task
class TestAgent(EvidenceAgent):
    role = "test_agent"
    def analyze(self, task: Task) -> Result:
        report = task.evidence.get("junit", {})
        failures = int(report.get("failures", 0)) + int(report.get("errors", 0))
        return Result(task_id=task.id, role=self.role, status="ok" if not failures else "failed", summary="Tests passed." if not failures else f"Tests failed ({failures} failures/errors).", evidence={"junit": report})
