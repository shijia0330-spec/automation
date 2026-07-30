from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def prompt_if_missing(value: str | None, label: str) -> str:
    if value:
        return value
    typed = input(f"{label}: ").strip()
    return typed if typed else "N/A"


def build_test_skeleton(
    test_id: str,
    test_name_slug: str,
    page_name: str,
    test_object: str,
    scenario: str,
) -> str:
    return f"""import pytest


@pytest.mark.smoke
def test_{test_name_slug}(page):
    # {test_id}
    # Page Name: {page_name}
    # Test Object: {test_object}
    # Scenario: {scenario}
    # TODO: Move steps from recorded script into page-object methods.
    # TODO: Add assertions that match expected behavior.
    raise NotImplementedError("Implement this testcase from recorded steps")
"""


def metadata_header(test_id: str, page_name: str, test_object: str, scenario: str) -> str:
    return (
        f"# Test Case ID: {test_id}\n"
        f"# Page Name: {page_name}\n"
        f"# Test Object: {test_object}\n"
        f"# Scenario: {scenario}\n\n"
    )


def prepend_metadata_if_record_exists(
    recorded_file: Path, test_id: str, page_name: str, test_object: str, scenario: str
) -> None:
    if not recorded_file.exists():
        print("[warn] Recorded script not found. No metadata header added.")
        return

    content = recorded_file.read_text(encoding="utf-8")
    if content.startswith("# Test Case ID:"):
        print("[info] Metadata header already exists in recorded script.")
        return

    recorded_file.write_text(
        metadata_header(test_id, page_name, test_object, scenario) + content,
        encoding="utf-8",
    )
    print("[info] Added metadata header to recorded script.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Playwright codegen and save output by testcase ID."
    )
    parser.add_argument("test_id", help="Testcase ID, for example: TC_001")
    parser.add_argument("url", help="Target URL for Playwright codegen")
    parser.add_argument("--page-name", help="Page name for this testcase metadata")
    parser.add_argument("--test-object", help="Test object/scope for this testcase")
    parser.add_argument("--scenario", help="Scenario summary for this testcase")
    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="Do not prompt for missing metadata; use N/A instead.",
    )
    parser.add_argument(
        "--target",
        default="python",
        help="Playwright codegen target (default: python)",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    recordings_dir = root / "pages" / "recordings"
    tests_dir = root / "tests"
    recordings_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    test_id_slug = slugify(args.test_id)
    recorded_file = recordings_dir / f"record_{test_id_slug}.py"
    test_file = tests_dir / f"test_{test_id_slug}.py"
    test_func_slug = f"{test_id_slug}_recorded_flow"

    if args.no_prompt:
        page_name = args.page_name or "N/A"
        test_object = args.test_object or "N/A"
        scenario = args.scenario or "N/A"
    else:
        page_name = prompt_if_missing(args.page_name, "Page Name")
        test_object = prompt_if_missing(args.test_object, "Test Object")
        scenario = prompt_if_missing(args.scenario, "Scenario")

    cmd = [
        "python3",
        "-m",
        "playwright",
        "codegen",
        "--target",
        args.target,
        "-o",
        str(recorded_file),
        args.url,
    ]

    print(f"[info] Starting recorder for {args.test_id}")
    print(f"[info] Recorded file: {recorded_file}")
    print("[info] Close recorder/press Ctrl+C when finished.")

    subprocess.run(cmd, check=False)
    prepend_metadata_if_record_exists(
        recorded_file=recorded_file,
        test_id=args.test_id,
        page_name=page_name,
        test_object=test_object,
        scenario=scenario,
    )

    if not test_file.exists():
        test_file.write_text(
            build_test_skeleton(
                args.test_id,
                test_func_slug,
                page_name,
                test_object,
                scenario,
            ),
            encoding="utf-8",
        )
        print(f"[info] Created test skeleton: {test_file}")
    else:
        print(f"[info] Test skeleton already exists: {test_file}")

    print("[done] Recording workflow complete.")


if __name__ == "__main__":
    main()
