"""Tests for the greet.py CLI (Issue #1)."""

import subprocess
import sys
from pathlib import Path

import greet

GREET_SCRIPT = Path(__file__).resolve().parent.parent / "greet.py"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    """Run the real CLI and return the completed process."""
    return subprocess.run(
        [sys.executable, str(GREET_SCRIPT), *args],
        capture_output=True,
        text=True,
        check=True,
    )


def test_cli_with_name() -> None:
    result = run_cli("Orbi")
    assert result.stdout == "Hello, Orbi!\n"


def test_cli_without_name() -> None:
    result = run_cli()
    assert result.stdout == "Hello, world!\n"


def test_main_prints_greeting(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["greet.py", "Orbi"])
    greet.main()
    assert capsys.readouterr().out == "Hello, Orbi!\n"

    monkeypatch.setattr(sys, "argv", ["greet.py"])
    greet.main()
    assert capsys.readouterr().out == "Hello, world!\n"
