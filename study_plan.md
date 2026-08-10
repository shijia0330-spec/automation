# API Automation Study Plan (2 Weeks)

## How to Use This Plan
- Spend 60-90 minutes per day.
- Mark each checkbox when completed.
- After each session, add 3 short bullets to `learning_notes.md`.

## Daily Routine (60-90 min)
- [ ] 15 min: Read one concept
- [ ] 35 min: Implement in this repo
- [ ] 20 min: Run tests and debug
- [ ] 10 min: Write learning notes

## Week 1 - Fundamentals

### Day 1 - Pytest Basics
- [x] Learn `assert`, `-q`, `-k`, `-m`
- [x] Run specific tests from `test_api_crud.py`
- [x] Practice fixing one failing test

### Day 2 - API Request Structure
- [x] Review path params, query params, headers, body
- [x] Add one query-based test
- [x] Add timeout handling expectation

### Day 3 - CRUD Positive Cases
- [x] Verify create/read/update/delete tests
- [x] Reuse fixture data instead of hardcoded duplicates
- [x] Keep smoke markers consistent

### Day 4 - Parametrize and Fixtures
- [x] Add at least 2 parametrized tests
- [x] Add/clean fixture usage in CRUD tests
- [x] Remove duplicated setup blocks

### Day 5 - Response Validation
- [x] Validate keys exist (`id`, `userId`, `title`, `completed`)
- [x] Validate data types where possible
- [x] Add one helper-style assertion pattern

### Day 6 - Negative Scenarios
- [x] Add invalid ID test for read
- [x] Add invalid payload-type test for patch/update
- [x] Document expected mock API behavior (200 vs 404 cases)

### Day 7 - Review and Refactor
- [x] Refactor messy test names/comments
- [x] Remove dead commented code
- [x] Ensure local test collection is clean

## Week 2 - Project Workflow

### Day 8 - Client Layer Quality
- [x] Review `api_client/base_client.py`
- [x] Keep naming consistent in `todos_client.py`
- [x] Add/update helper methods only when needed by tests

### Day 9 - Test Suite Strategy
- [x] Review smoke/negative split
- [x] Make sure markers are used intentionally
- [x] Run marker-specific commands

### Day 10 - CI Understanding
- [x] Read `.github/workflows/api-tests.yml`
- [x] Map each step to local command equivalent
- [x] Reproduce one CI command locally

### Day 11 - CI Debugging Practice
- [x] Trigger a test run from a small commit
- [x] If fail, identify failing step and root cause
- [x] Fix and rerun to green

### Day 12 - Reporting Basics
- [x] Generate simple pytest output summary
- [x] Save key run observations in notes
- [x] Track common failure patterns

### Day 13 - Stability Improvements
- [x] Review flaky risks (hardcoded assumptions/data)
- [x] Improve deterministic assertions
- [x] Avoid over-strict checks for mock API behavior

### Day 14 - Portfolio Polish
- [x] Update README with test commands
- [x] Confirm CI status is passing
- [x] Final cleanup commit with clear message

## Milestones
- [x] End Week 1: Clean CRUD + negative suite with fixtures and parametrize
- [x] End Week 2: Stable CI workflow and polished automation project

## Useful Commands
- Run one file: `pytest -q test_api_crud.py`
- Collect only: `pytest --collect-only -q test_api_*.py`
- Run smoke tests: `pytest -m smoke -q test_api_*.py`
- Run negative tests: `pytest -m negative -q test_api_*.py`
- Check git changes: `git status`
