"""Print the excuse line for the make.fun entry.

The excuse lives in entry.txt next to this script; this file only loads it
and prints it, with a fallback line if the file is missing or blank.
"""

from pathlib import Path


def load_excuse():
    """Read the excuse from entry.txt next to this script."""
    try:
        text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return "I would explain, but the explanation is still compiling."
    return text or "I would explain, but the explanation is still compiling."


def main():
    print(load_excuse())


if __name__ == "__main__":
    main()
