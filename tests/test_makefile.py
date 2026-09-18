"""Tests for the Makefile ``test`` target (Issue #6)."""

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_make(*args: str) -> subprocess.CompletedProcess:
    """Run ``make`` in the repository root and return the completed process."""
    return subprocess.run(
        ["make", "-C", str(REPO_ROOT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_make_test_runs_pytest() -> None:
    """``make test`` runs pytest and reports its summary."""
    result = run_make("test", "PYTEST_ARGS=tests/test_greet.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "passed" in result.stdout


def test_make_test_propagates_pytest_failure() -> None:
    """A failing pytest run makes ``make test`` fail too."""
    result = run_make("test", "PYTEST_ARGS=tests/does_not_exist.py")
    assert result.returncode != 0
    assert "ERROR" in result.stdout or "ERROR" in result.stderr
