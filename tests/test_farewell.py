"""Tests for the farewell.py CLI (Issue #5)."""

import subprocess
import sys
from pathlib import Path

import farewell

FAREWELL_SCRIPT = Path(__file__).resolve().parent.parent / "farewell.py"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    """Run the real CLI and return the completed process."""
    return subprocess.run(
        [sys.executable, str(FAREWELL_SCRIPT), *args],
        capture_output=True,
        text=True,
        check=True,
    )


def test_cli_with_name() -> None:
    result = run_cli("Orbi")
    assert result.stdout == "Goodbye, Orbi!\n"


def test_cli_without_name() -> None:
    result = run_cli()
    assert result.stdout == "Goodbye, world!\n"


def test_farewell_returns_message() -> None:
    assert farewell.farewell("Orbi") == "Goodbye, Orbi!"


def test_main_prints_farewell(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["farewell.py", "Orbi"])
    farewell.main()
    assert capsys.readouterr().out == "Goodbye, Orbi!\n"

    monkeypatch.setattr(sys, "argv", ["farewell.py"])
    farewell.main()
    assert capsys.readouterr().out == "Goodbye, world!\n"


def test_cli_failure_on_missing_file() -> None:
    """The real user failure path: wrong cwd gives a concrete Python error."""
    missing = FAREWELL_SCRIPT.parent / "does-not-exist" / "farewell.py"
    result = subprocess.run(
        [sys.executable, str(missing)],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "No such file or directory" in result.stderr
