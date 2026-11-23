from __future__ import annotations
def require_approval(action: str) -> bool:
    """Human gate for actions beyond the pre-approved rollback path."""
    return input(f"Approve action: {action} [y/N] ").strip().lower() == "y"
