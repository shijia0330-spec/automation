# Learning Notes

## Bugs I Fixed
- Used wrong query parameter names (`start`, `limit`, `sortId`) and corrected to JSONPlaceholder keys (`_start`, `_limit`, `_sort`, `_order`).
- Fixed assertion comparing a single value to a list (`ids[0] == sorted(ids)`), changed to full-list comparison (`ids == sorted(ids)`).
- Fixed syntax errors in `requests.get(...)` calls (missing comma before `params`, wrong `TIMEOUT` argument name).

## Patterns I Learned
- Use `params={...}` with `requests.get()` for cleaner and safer query handling.
- Always add `timeout=TIMEOUT` to avoid hanging tests.
- For pagination overlap checks, collect IDs into sets and use `isdisjoint()`.

## Learn helper 
- Created and used get_posts(params) helper to reduce duplicate request code.”
- Keep one consistent style across files (params + timeout + clean assertions).
- Moved get_posts into utils/api_client.py and reused across tests.
- query value formatting matters ("true" vs True) when filtering APIs.
- "true" vs True in query params
- `pytest.mark.parametrize` helps test multiple inputs in one test without duplicate code.
- For `_limit` boundary checks, choose representative values (small/typical/larger) like `1`, `5`, and `20`.

## CRUD and Negative Tests
- `PUT` and `PATCH` are update requests, so they need two things: target ID + payload body.
- `todo_id` tells which record to update; payload tells what fields/values to change.
- Calling `patch_todo(9999)` without payload is invalid usage because function signature requires `patch_todo(todo_id, todo)`.
- On JSONPlaceholder (mock API), invalid update/patch IDs may still return `200` instead of `404`.
- For this mock API, negative tests should validate observed behavior (for example response echo) instead of assuming strict validation codes.
- If we specifically want a `404` expectation, `get_todo_by_id(999999)` is a better case than `PATCH/PUT`.

## Common Failure Patterns
- Import mismatch causes collection errors (example: test imports function name not defined in client file).
- Wrong method signature usage causes runtime test errors (example: calling `patch_todo(id)` without payload).
- Expecting strict status codes on mock APIs causes false failures (example: PATCH invalid id still returns `200`).
- Outdated CI run/old commit can show already-fixed errors, so always verify the run commit hash first.

## Flaky Risk Review
- Hardcoded exact title/content from live public API can change and make assertions brittle.
- Overly strict body equality on endpoints with mock behavior can fail unexpectedly.
- More stable pattern: assert required keys, types, and core behavior instead of fragile full-response matching.
