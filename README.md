# API Automation Practice

Basic API test automation project using `pytest` and `requests`.

## CI Status

![API Tests](https://github.com/shijia0330-spec/Automation/actions/workflows/api-tests.yml/badge.svg)

## Project Structure

- `api_client/todos_client.py` - API helper functions
- `test_api_smoke.py` - smoke + negative API tests
- `pytest.ini` - pytest marker configuration
- `.github/workflows/api-tests.yml` - GitHub Actions CI workflow

## Setup

```bash
python3 -m pip install --upgrade pip
python3 -m pip install pytest requests
```

## Run Tests Locally

Run all:

```bash
pytest test_api_smoke.py
```

Run smoke only:

```bash
pytest -m smoke test_api_smoke.py
```

Run negative only:

```bash
pytest -m negative test_api_smoke.py
```

## Notes

- `smoke` tests validate core positive API behavior.
- `negative` tests validate invalid endpoint behavior.
- CI runs on every push and pull request.
