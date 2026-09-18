"""Print a greeting for a name.

Usage:
    python greet.py          # Hello, world!
    python greet.py Orbi     # Hello, Orbi!
"""

import sys


def greet(name: str) -> str:
    """Return the greeting line for ``name``."""
    return f"Hello, {name}!"


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))


if __name__ == "__main__":  # pragma: no cover
    main()
