# OrangeHRM UI Automation Framework

This project uses Python, Selenium, and pytest to open the OrangeHRM website in a web browser and check a few common actions automatically. You can run the checks yourself from a terminal, or let the included GitHub Actions workflow run them when code is pushed.

## What the framework checks

- **Login check:** Logs in using the environment account and checks that the OrangeHRM home page opens.
- **Multiple-user login check:** Runs the login check once for every entry in the `users` section of `config/config.json`.
- **PIM employee search:** Opens the PIM (Personal Information Management) area and checks for the employee used by the test.
- **PIM employee creation:** Enters generated employee details in the Add Employee form.

The tests use the public OrangeHRM demo site, so an internet connection is required. The PIM tests interact with shared demo data; use an environment that is safe to modify if you change the target URL.

## How the project is organized

| Path | Purpose |
| --- | --- |
| `tests/` | pytest test cases that describe what should be checked. |
| `pages/` | Page Objects: reusable methods for interacting with the login and PIM pages. Tests call these methods instead of locating every browser element themselves. |
| `locators/` | Names and browser selectors for fields, buttons, and other page elements. |
| `utilities/config_reader.py` | Reads the JSON configuration file. |
| `utilities/screenshot.py` | Saves timestamped browser screenshots. |
| `utilities/logger.py` | Sets up the framework's file logger. |
| `config/config.json` | Website environments and the accounts used by the multiple-user login test. |
| `conftest.py` | Shared pytest setup, including browser creation, command-line options, and the environment login fixture. |
| `pytest.ini` | Default pytest options, test markers, and report output locations. |
| `.github/workflows/test_suite.yml` | GitHub Actions workflow for running pytest automatically. |

## Requirements

Before starting, install:

1. **Python 3.10 or newer.** Selenium 4.50 requires Python 3.10 or newer.
2. **Google Chrome**, installed on the computer that will run the tests.
3. **Internet access** to reach the OrangeHRM demo site.

Selenium 4 uses Selenium Manager to find or obtain a compatible Chrome driver in most setups; a separate driver installation is usually not needed.

## Setup on Windows

Open PowerShell in the project folder (the folder containing `requirements.txt`) and run:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell does not allow activation, you can skip activation and invoke the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The project pins its Python package versions in `requirements.txt`. Installing that file provides Selenium, pytest, and the pytest plugins used for HTML and Allure reports.

## Configure the tests

Edit `config/config.json` to set the website URL and the login accounts. The file has two kinds of entries:

- `qa`, `dev`, and `stage` each contain a `url`, `username`, and `password`. The shared `orange_hrm_login` fixture reads the selected environment. Select one with the `--env` option.
- `users` is a collection of named accounts used only by `test_hrm_multi_login`. Each entry needs a `username` and `password`. pytest uses each key as the test case's readable ID.

For example, the structure is:

```json
{
  "qa": {
    "url": "https://example.test/",
    "username": "your-test-account",
    "password": "your-test-password"
  },
  "users": {
    "account_one": {
      "username": "first-test-account",
      "password": "first-test-password"
    },
    "account_two": {
      "username": "second-test-account",
      "password": "second-test-password"
    }
  }
}
```

Keep real or private credentials out of source control. The accounts in the checked-in configuration are demo/test values; replace them with accounts valid for the website you are testing. The current multiple-user entries may be aliases for the same demo account, so add distinct credentials if you need to test distinct users.

## Run the tests

With the virtual environment active, run all tests:

```powershell
python -m pytest
```

Common alternatives:

```powershell
# Run without displaying a browser window
python -m pytest --headless

# Use the qa/dev/stage account and URL selected from config/config.json
python -m pytest --env qa
python -m pytest --env dev
python -m pytest --env stage

# Run only the tests in one file
python -m pytest tests/test_login.py
python -m pytest tests/test_pim_search_and_create_user.py

# Run tests marked smoke or regression
python -m pytest -m smoke
python -m pytest -m regression

# List tests without running them
python -m pytest --collect-only
```

`--headless` hides the browser window. Without it, Chrome opens visibly. The `--env` option selects the environment credentials used by tests that request `orange_hrm_login`; the multiple-user login test reads directly from `users` and is not changed by `--env`. At present, the login page object navigates to the public OrangeHRM demo URL directly, so changing an environment's `url` does not yet change the final login destination.

pytest is configured to stop after three failures, show test details, and write reports. You do not need to add these settings to the commands above.

## Test results and generated files

- **HTML test report:** `reports/report.html`. Open this file in a browser to view the pytest results.
- **Allure result data:** `reports/allure-results/`. This is raw result data, not a rendered report. If the Allure command-line tool is installed, render or view it with `allure serve reports/allure-results`.
- **Screenshots:** `screenshots/`. Screenshot files include a timestamp in their names.
- **Logs:** `logs/automation.log`. The framework records test and browser activity here.

These folders are created or updated when tests run. The HTML report is generated by pytest-html; Allure report rendering requires the separate Allure command-line tool.

## GitHub Actions

The workflow in `.github/workflows/test_suite.yml` runs `pytest` on pushes and pull requests targeting `main`, and on its scheduled run. A run can be viewed under the repository's **Actions** tab. The workflow currently selects Python 3.9.20, which is below Selenium's stated minimum version; update the workflow to Python 3.10 or newer for dependency installation to be compatible.

The workflow currently attempts to upload `report.html`, while pytest writes the report to `reports/report.html`. The test run may therefore succeed even if the HTML report artifact is not uploaded; use the local report path above when running the suite locally.

## Troubleshooting

- **`unrecognized arguments: --headless`:** Run pytest from the project root so it loads this project's `conftest.py` and `pytest.ini`. The flag is optional; omit it to show Chrome.
- **Chrome or driver startup fails:** Confirm Chrome is installed, internet access is available, and Selenium can download/find a compatible driver.
- **Login fails:** Check the selected `--env`, the matching section in `config/config.json`, and that the configured account can access the target site.
- **A PIM search fails:** The search test currently expects a particular employee record in the demo data. Shared demo data can change, so verify the employee and the selectors in `pages/pim_page.py` and `locators/locators.py`.
- **A test fails after the site changes:** Page selectors are maintained in `locators/locators.py`; update them to match the current OrangeHRM page.
