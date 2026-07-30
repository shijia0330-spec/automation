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
