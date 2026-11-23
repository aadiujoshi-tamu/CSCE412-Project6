from pathlib import Path
from .base import EvidenceAgent, Result, Task
class PipelineEngineer(EvidenceAgent):
    role = "pipeline_engineer"
    def analyze(self, task: Task) -> Result:
        required = ["pipeline/pipeline.json", "pipeline/buildspec-build.yml", "pipeline/buildspec-deploy.yml", "pipeline/buildspec-verify.yml"]
        missing = [p for p in required if not Path(p).is_file()]
        return Result(task_id=task.id, role=self.role, status="failed" if missing else "ok", summary="Pipeline configuration is complete." if not missing else "Pipeline configuration is incomplete.", evidence={"missing": missing})
