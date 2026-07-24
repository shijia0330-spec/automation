# Web Automation Learning Folder

This folder is a clean starter template for learning web UI automation with Python.

## Stack

- `pytest` for test runner
- `playwright` for browser automation

## Structure

- `pages/` page objects
- `tests/` test files and fixtures
- `pytest.ini` local markers
- `requirements.txt` dependencies

## Setup

```bash
cd web_automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests

```bash
pytest -m smoke -q
```

Run with visible browser window:

```bash
pytest -m smoke --show-browser -q
```

## Learning path

1. Start with `tests/test_login_demo.py`.
2. Add one new page object under `pages/`.
3. Add one happy-path and one negative test for each page.
