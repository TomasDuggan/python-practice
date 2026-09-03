#!/usr/bin/env python3
"""Use: python new_problem.py <folder-name>"""

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print("Use: python new_problem.py <folder-name>  (eg: 001-fibonacci)")
        sys.exit(1)

    name = sys.argv[1]
    target = Path("problems") / name

    if target.exists():
        print(f"Error: {target} already exists.")
        sys.exit(1)

    target.mkdir(parents=True)

    for filename in ("problem.md", "solution.py", "test_solution.py"):
        (target / filename).touch()

    print(f"Created: {target}/")
    print("  - problem.md")
    print("  - solution.py")
    print("  - test_solution.py")


if __name__ == "__main__":
    main()