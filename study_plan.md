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

## Next Track - Advanced Validation

### Session A - Reusable Schema Practice
- [x] Add post schema helper (`assert_post_schema`)
- [x] Apply post schema checks in sorting/query tests
- [x] Add reusable list validator (`assert_schema_list(data, schema_assertion)`)
- [x] Replace duplicated schema loops with list validator helper
- [x] Add clear custom assertion messages for faster debugging

### Session B - Consolidation
- [x] Run full suite (`pytest -q test_api_*.py`) after helper refactor
- [x] Record "before vs after" helper refactor notes in `learning_notes.md`
- [x] Final commit and CI green check for this advanced validation track

## Next Track - API Reliability and Security

### Session C - Headers, Timing, and Environments
- [x] Validate JSON content type and UTF-8 response encoding
- [x] Add a basic response-time threshold check
- [x] Configure API base URLs with environment variables
- [x] Run the full suite and confirm CI is green

### Session D - Authentication
- [x] Validate login returns a non-empty access token
- [x] Use a Bearer token to access the current-user endpoint
- [x] Test missing and invalid token responses
- [x] Validate authentication error messages are present
- [x] Record authentication lessons and confirm CI is green

### Session E - Multi-API Dependency Workflows
- [x] Create a fixture that logs in and returns an access token
- [x] Reuse the token fixture in protected endpoint tests
- [x] Practice a login -> authenticated request workflow
- [x] Keep dependent setup failures clear and isolated
- [ ] Run the full suite, update notes, and confirm CI is green

## Future Track - Intermediate API Automation

### Session F - Advanced Authentication and Secrets
- [ ] Test token refresh and expiration behavior
- [ ] Test role-based authorization and forbidden actions
- [ ] Review logout and token-revocation behavior
- [ ] Store credentials and tokens securely outside source code

### Session G - Mocking and Resilience
- [ ] Mock successful and failed API responses
- [ ] Simulate timeouts, connection errors, and invalid JSON
- [ ] Test `4xx` and `5xx` error-handling behavior
- [ ] Learn when retries are safe and when they are risky

### Session H - Contracts and Test Data
- [ ] Validate responses with JSON Schema or OpenAPI
- [ ] Create reusable test-data builders
- [ ] Add setup and cleanup for created test records
- [ ] Keep tests independent and deterministic

### Session I - Reporting and Framework Quality
- [ ] Generate JUnit or HTML test reports
- [ ] Add useful logging without exposing secrets
- [ ] Organize configuration, clients, fixtures, helpers, and tests
- [ ] Run suitable tests in parallel

### Session J - Performance and Final Project
- [ ] Learn basic load and performance testing
- [ ] Measure averages and percentiles such as p95
- [ ] Build one complete portfolio API automation project
- [ ] Run the final suite in CI and document the framework

## Parallel Track - Playwright with Python

Start this track after completing API Session E. Continue one intermediate API session each week while learning UI automation.

### Playwright Week 1 - Browser Basics
- [ ] Install Playwright and its browsers
- [ ] Open a page and understand browser, context, and page
- [ ] Practice stable locators
- [ ] Click, fill, select, and submit
- [ ] Add basic UI assertions

### Playwright Week 2 - Reliable UI Tests
- [ ] Learn auto-waiting and avoid fixed sleeps
- [ ] Test forms, navigation, dialogs, and new tabs
- [ ] Use pytest fixtures for browser setup
- [ ] Capture screenshots and traces for failures

### Playwright Week 3 - Framework Structure
- [ ] Create Page Object Model classes
- [ ] Separate test data, page actions, and assertions
- [ ] Reuse login/setup state safely
- [ ] Add positive and negative UI scenarios

### Playwright Week 4 - CI and Portfolio
- [ ] Run tests across Chromium, Firefox, and WebKit
- [ ] Add Playwright tests and artifacts to CI
- [ ] Create one end-to-end business workflow
- [ ] Document commands, structure, and debugging steps

### Balanced Weekly Schedule
- [ ] 3 days: Playwright with Python
- [ ] 2 days: intermediate API automation
- [ ] 1 day: review, debugging, and project practice
- [ ] 1 day: rest

## Useful Commands
- Run one file: `pytest -q test_api_crud.py`
- Collect only: `pytest --collect-only -q test_api_*.py`
- Run smoke tests: `pytest -m smoke -q test_api_*.py`
- Run negative tests: `pytest -m negative -q test_api_*.py`
- Check git changes: `git status`
