from __future__ import annotations

import argparse
import re
from pathlib import Path


REQ_PATTERN = re.compile(r"\*\*(R\d+):")
REQ_SECTION_PATTERN = re.compile(r"^###\s+(R\d+)\s+-")
TESTCASE_PATTERN = re.compile(r"\*\*(TC-\d+)\*\*\s+\(([^)]+)\)")


def parse_requirements(requirements_path: Path) -> list[str]:
    text = requirements_path.read_text(encoding="utf-8")
    ids = REQ_PATTERN.findall(text)
    # Keep order, remove duplicates.
    seen: set[str] = set()
    ordered: list[str] = []
    for req_id in ids:
        if req_id not in seen:
            seen.add(req_id)
            ordered.append(req_id)
    return ordered


def parse_testcases(testcase_list_path: Path) -> dict[str, list[tuple[str, str]]]:
    mapping: dict[str, list[tuple[str, str]]] = {}
    current_req: str | None = None

    for raw_line in testcase_list_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        req_section = REQ_SECTION_PATTERN.match(line)
        if req_section:
            current_req = req_section.group(1)
            mapping.setdefault(current_req, [])
            continue

        tc_match = TESTCASE_PATTERN.search(line)
        if tc_match and current_req:
            tc_id = tc_match.group(1)
            type_block = tc_match.group(2)
            tc_type = type_block.split(",")[0].strip().lower()
            mapping[current_req].append((tc_id, tc_type))

    return mapping


def summarize(
    requirement_ids: list[str], testcase_mapping: dict[str, list[tuple[str, str]]]
) -> str:
    out: list[str] = []
    uncovered: list[str] = []
    missing_pos_neg: list[str] = []
    missing_boundary: list[str] = []

    out.append("Coverage Report")
    out.append("=" * 40)
    out.append(f"Requirements found: {len(requirement_ids)}")
    total_cases = sum(len(v) for v in testcase_mapping.values())
    out.append(f"Mapped testcase entries: {total_cases}")
    out.append("")

    for req_id in requirement_ids:
        cases = testcase_mapping.get(req_id, [])
        if not cases:
            uncovered.append(req_id)
            out.append(f"- {req_id}: ❌ no mapped testcases")
            continue

        tc_ids = ", ".join(tc_id for tc_id, _ in cases)
        types = {tc_type for _, tc_type in cases}

        has_positive = "positive" in types
        has_negative = "negative" in types
        has_boundary = "boundary" in types

        status = "✅"
        notes: list[str] = []
        if not has_positive or not has_negative:
            status = "⚠️"
            missing_pos_neg.append(req_id)
            notes.append("missing positive/negative balance")
        if not has_boundary:
            missing_boundary.append(req_id)
            notes.append("no boundary case")

        note_text = f" ({'; '.join(notes)})" if notes else ""
        out.append(f"- {req_id}: {status} {len(cases)} cases [{tc_ids}]{note_text}")

    out.append("")
    out.append("Gaps")
    out.append("-" * 40)
    out.append(f"Uncovered requirements: {uncovered if uncovered else 'None'}")
    out.append(
        "Requirements missing positive/negative balance: "
        f"{missing_pos_neg if missing_pos_neg else 'None'}"
    )
    out.append(
        f"Requirements with no boundary case: {missing_boundary if missing_boundary else 'None'}"
    )
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check requirement-to-testcase coverage from markdown files."
    )
    parser.add_argument(
        "--requirements",
        default="ai_practice/requirements.md",
        help="Path to requirements markdown file",
    )
    parser.add_argument(
        "--testcases",
        default="ai_practice/testcase_list.md",
        help="Path to testcase list markdown file",
    )
    args = parser.parse_args()

    requirements_path = Path(args.requirements)
    testcase_list_path = Path(args.testcases)

    if not requirements_path.exists():
        raise FileNotFoundError(f"Requirements file not found: {requirements_path}")
    if not testcase_list_path.exists():
        raise FileNotFoundError(f"Testcase file not found: {testcase_list_path}")

    requirement_ids = parse_requirements(requirements_path)
    testcase_mapping = parse_testcases(testcase_list_path)
    print(summarize(requirement_ids, testcase_mapping))


if __name__ == "__main__":
    main()
