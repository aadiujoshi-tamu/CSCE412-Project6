from pathlib import Path

def test_repository_pipeline_layout():
    for directory in ("agents", "scripts", "pipeline", "tests"):
        assert Path(directory).is_dir()
