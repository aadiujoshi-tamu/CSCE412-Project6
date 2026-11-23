from .base import EvidenceAgent, Result, Task
class DiagnosisAgent(EvidenceAgent):
    role = "diagnosis_agent"
    def analyze(self, task: Task) -> Result:
        logs = str(task.evidence.get("logs", ""))[-4000:]
        return Result(task_id=task.id, role=self.role, status="ok", summary="Diagnosis is based on the supplied build and verification evidence.", evidence={"log_excerpt": logs, "junit": task.evidence.get("junit", {}), "verification": task.evidence.get("verification", {})})
