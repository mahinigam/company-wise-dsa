"""Run inline examples in every DSA solution using only the Python standard library."""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"


def main() -> int:
    files = sorted(PROBLEMS.rglob("*.py"))
    failures = []
    for path in files:
        try:
            runpy.run_path(str(path), run_name="__dsa_examples__")
        except Exception as exc:  # report all failures instead of stopping early
            failures.append((path.relative_to(ROOT), exc))
    if failures:
        for path, exc in failures:
            print(f"FAIL {path}: {type(exc).__name__}: {exc}")
        return 1
    print(f"PASS: {len(files)} solution modules and their inline examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
