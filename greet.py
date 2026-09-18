"""Print a greeting for a name.

Usage:
    python greet.py               # Hello, world!
    python greet.py Orbi          # Hello, Orbi!
    python greet.py --shout Orbi  # HELLO, ORBI!
    python greet.py --version     # greet.py 0.1.0
"""

import sys

__version__ = "0.1.0"


def greet(name: str, shout: bool = False) -> str:
    """Return the greeting line for ``name``, upper-cased when ``shout``."""
    message = f"Hello, {name}!"
    return message.upper() if shout else message


def main() -> None:
    args = sys.argv[1:]
    if "--version" in args:
        print(f"greet.py {__version__}")
        return
    shout = "--shout" in args
    if shout:
        args = [arg for arg in args if arg != "--shout"]
    name = args[0] if args else "world"
    print(greet(name, shout=shout))


if __name__ == "__main__":  # pragma: no cover
    main()
