"""Tests for the greet.py CLI (Issue #1, Issue #7)."""

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


def test_greet_shout_upper_cases() -> None:
    assert greet.greet("Orbi", shout=True) == "HELLO, ORBI!"


def test_greet_shout_defaults_to_false() -> None:
    assert greet.greet("Orbi") == "Hello, Orbi!"


def test_cli_shout_with_name() -> None:
    result = run_cli("--shout", "Orbi")
    assert result.stdout == "HELLO, ORBI!\n"


def test_cli_shout_after_name() -> None:
    result = run_cli("Orbi", "--shout")
    assert result.stdout == "HELLO, ORBI!\n"


def test_cli_shout_without_name() -> None:
    result = run_cli("--shout")
    assert result.stdout == "HELLO, WORLD!\n"


def test_main_prints_greeting(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["greet.py", "Orbi"])
    greet.main()
    assert capsys.readouterr().out == "Hello, Orbi!\n"

    monkeypatch.setattr(sys, "argv", ["greet.py"])
    greet.main()
    assert capsys.readouterr().out == "Hello, world!\n"


def test_main_prints_shouted_greeting(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["greet.py", "--shout", "Orbi"])
    greet.main()
    assert capsys.readouterr().out == "HELLO, ORBI!\n"

    monkeypatch.setattr(sys, "argv", ["greet.py", "Orbi", "--shout"])
    greet.main()
    assert capsys.readouterr().out == "HELLO, ORBI!\n"

    monkeypatch.setattr(sys, "argv", ["greet.py", "--shout"])
    greet.main()
    assert capsys.readouterr().out == "HELLO, WORLD!\n"
