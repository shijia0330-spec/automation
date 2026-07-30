---
name: qa-testcase-generator
description: Generate a testcase list from requirements markdown with requirement traceability, positive/negative/boundary coverage, and uncovered requirement reporting. Use when the user asks to create testcases from requirements.md or similar product requirement documents.
disable-model-invocation: true
---

# QA Testcase Generator

## Purpose

Create testcases from requirement documents in a consistent, review-ready format.

## When To Use

Use this skill when the user asks to:
- generate testcases from `requirements.md`
- create a testcase table for QA review
- check if any requirement is missing testcase coverage

## Inputs

- Requirement source markdown (for example `ai_practice/requirements.md`)
- Optional existing testcase file (for example `ai_practice/testcase_list.md`)

If the requirement file path is unclear, ask before generating.

## Output Format

Generate a markdown table with this exact column order:

`Test ID | Requirement ID | Type | Priority | Scenario | Precondition | Steps | Expected Behaviour`

Also include:
- `Coverage Summary` (requirement ID -> testcase IDs)
- `Uncovered Requirements` (if none, write `None`)

## Generation Rules

1. Include all three testcase types:
   - Positive
   - Negative
   - Boundary
2. Create at least 2 testcases per requirement ID.
3. Keep scenarios unique (no duplicates or near-duplicates).
4. Write expected behaviour as specific, testable outcomes.
5. Mark blocking behaviors as high priority when critical checkout data is missing.

## Workflow

1. Read and list all requirement IDs from the requirement file.
2. Generate testcase candidates per requirement.
3. Remove overlap and weak/vague expected results.
4. Validate each requirement has at least 2 mapped tests.
5. Produce final table, then add coverage and uncovered sections.

## Quality Checklist

- Every requirement ID appears in Coverage Summary.
- Every requirement has positive or baseline validation.
- Negative and boundary cases are represented where relevant.
- No requirement is left unmapped.

## Example Request

`Generate testcase list from ai_practice/requirements.md and update ai_practice/testcase_list.md`
