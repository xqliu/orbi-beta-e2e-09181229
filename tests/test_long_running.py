"""Integration test that simulates a long-running check (Issue #9)."""

import time

import greet


def test_long_running_greeting() -> None:
    # Real wall-clock slow check: 1020 seconds = 17 minutes.
    time.sleep(1020)
    assert greet.greet("Orbi") == "Hello, Orbi!"
