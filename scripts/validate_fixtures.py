"""Validate SENTINEL JSON evaluation fixtures without third-party dependencies."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "tests" / "fixtures"

REQUIRED_TOP_LEVEL = {"schema_version", "run_id", "agent", "evaluator", "results"}
REQUIRED_RESULT = {"scenario_id", "category", "risk", "status", "failure_type", "tool_calls"}
VALID_RISKS = {"low", "medium", "high", "critical"}
VALID_STATUS = {"pass", "fail"}


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON ({exc})"]

    missing = REQUIRED_TOP_LEVEL - data.keys()
    if missing:
        errors.append(f"{path}: missing top-level fields: {sorted(missing)}")

    if not isinstance(data.get("results"), list) or not data["results"]:
        errors.append(f"{path}: results must be a non-empty list")
        return errors

    for index, result in enumerate(data["results"]):
        missing_result = REQUIRED_RESULT - result.keys()
        if missing_result:
            errors.append(f"{path}: result {index} missing {sorted(missing_result)}")
        if result.get("risk") not in VALID_RISKS:
            errors.append(f"{path}: result {index} has invalid risk")
        if result.get("status") not in VALID_STATUS:
            errors.append(f"{path}: result {index} has invalid status")
        if not isinstance(result.get("tool_calls"), int) or result.get("tool_calls", -1) < 0:
            errors.append(f"{path}: result {index} tool_calls must be a non-negative integer")

    return errors


def main() -> int:
    files = sorted(FIXTURE_DIR.glob("*.json"))
    if not files:
        print("No JSON fixtures found.")
        return 1

    errors = [error for path in files for error in validate_file(path)]
    if errors:
        print("Fixture validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Validated {len(files)} SENTINEL fixture(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
