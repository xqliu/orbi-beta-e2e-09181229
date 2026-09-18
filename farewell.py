"""Print a farewell for a name.

Usage:
    python farewell.py           # Goodbye, world!
    python farewell.py Orbi      # Goodbye, Orbi!
"""

import sys


def farewell(name: str) -> str:
    """Return the farewell line for ``name``."""
    return f"Goodbye, {name}!"


def main() -> None:
    args = sys.argv[1:]
    name = args[0] if args else "world"
    print(farewell(name))


if __name__ == "__main__":  # pragma: no cover
    main()
