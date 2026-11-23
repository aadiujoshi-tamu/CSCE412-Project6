from .base import EvidenceAgent, Result, Task
class VerificationAgent(EvidenceAgent):
    role = "verification_agent"
    def analyze(self, task: Task) -> Result:
        checks = task.evidence.get("checks", {})
        failed = [name for name, passed in checks.items() if not passed]
        return Result(task_id=task.id, role=self.role, status="ok" if not failed else "failed", summary="Production verification passed." if not failed else "Production checks failed: " + ", ".join(failed), evidence={"checks": checks})
