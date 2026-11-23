from .base import EvidenceAgent, Result, Task
class RecoveryAgent(EvidenceAgent):
    role = "recovery_agent"
    def analyze(self, task: Task) -> Result:
        known_good = task.evidence.get("known_good_sha")
        if not known_good: return Result(task_id=task.id, role=self.role, status="failed", summary="No known-good release is available.", evidence=task.evidence)
        return Result(task_id=task.id, role=self.role, status="ok", summary=f"Bounded rollback may restore {known_good}.", evidence={"known_good_sha": known_good}, proposed_action=f"python scripts/rollback.py --sha {known_good}")
