# QualityCheck — UI & API Test Automation

A Python-based test automation project using **Playwright, pytest, and Requests** to validate web application behavior and REST API responses. The project includes reusable page objects, parametrized tests, HTML reporting, and a GitHub Actions CI workflow.

**Repository:** [github.com/nawtfound404/QualityCheck](https://github.com/nawtfound404/QualityCheck)

## Features

- **UI automation:** Browser navigation, page-title validation, and form submission.
- **Page Object Model (POM):** Reusable page interactions and assertions.
- **Parametrized testing:** Execute the same test with multiple input values.
- **API testing:** Validate HTTP status codes and JSON response data.
- **HTML reports:** Generate a self-contained pytest HTML report.
- **CI automation:** Run tests automatically through GitHub Actions on pushes and pull requests.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Test implementation |
| Playwright | Browser automation |
| pytest | Test execution and assertions |
| pytest-playwright | Playwright integration with pytest |
| Requests | HTTP API testing |
| pytest-html | HTML test reports |
| Git & GitHub | Version control and collaboration |
| GitHub Actions | Continuous integration |

## Project Structure

```text
QualityCheck/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   ├── api/
│   │   └── test_posts_api.py
│   ├── pages/
│   │   └── web_form_page.py
│   ├── test_homepage.py
│   └── test_web_form.py
├── reports/
│   └── report.html
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nawtfound404/QualityCheck.git
cd QualityCheck
```

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install the Playwright browser

```bash
python -m playwright install chromium
```

On Ubuntu or other Linux distributions, install the required browser system dependencies if prompted:

```bash
python -m playwright install --with-deps chromium
```

## Running the Tests

### Run the complete test suite

```bash
python -m pytest -v
```

### Run UI tests

```bash
python -m pytest tests/test_homepage.py tests/test_web_form.py -v
```

### Run API tests

```bash
python -m pytest tests/api/test_posts_api.py -v
```

### Generate an HTML report

```bash
mkdir -p reports test-results

python -m pytest -v \
  --browser chromium \
  --html=reports/report.html \
  --self-contained-html \
  --screenshot=only-on-failure \
  --output=test-results
```

Open the report on Linux:

```bash
xdg-open reports/report.html
```

The report summarizes the latest test run. Failure screenshots and related browser output depend on the configured Playwright pytest options.

## Test Coverage

### UI Tests

The browser tests cover:

- Homepage title validation.
- Navigation to the Playwright installation page.
- Form submission with multiple text inputs.
- Text input value validation before submission.
- Verification of the success message after form submission.

### API Tests

The API tests use the public JSONPlaceholder service and cover:

- Successful retrieval of an existing post.
- Validation of HTTP status codes.
- Validation of response fields and data types.
- Handling of a request for a nonexistent post.

## Page Object Model

The `WebFormPage` class encapsulates page-specific locators and interactions, including opening the page, filling fields, submitting the form, and checking the resulting message.

This approach reduces duplicated browser interaction code and makes tests easier to maintain.

## Continuous Integration

GitHub Actions runs the test suite on pushes to `main`, pull requests targeting `main`, and manual workflow dispatches.

The workflow installs Python dependencies, sets up Chromium, executes the tests, generates an HTML report, and uploads the report as a workflow artifact.

View workflow runs: [GitHub Actions](https://github.com/nawtfound404/QualityCheck/actions)

## Current Validation

During development, the following results were observed:

- **7 tests passed** in a complete local test run.
- **4 form tests passed** in a subsequent form-specific run.
- The HTML report was generated successfully.
- The GitHub Actions workflow was reported working during project development.

These are development results, not a guarantee that every future run will pass.

## Future Improvements

- Add more negative and boundary-value test scenarios.
- Expand API coverage to additional methods and response cases.
- Improve test data management and configuration.
- Add clearer failure diagnostics and reporting.
- Expand browser and cross-browser coverage where appropriate.

## Disclaimer

This is a learning and portfolio project. The UI tests use public demonstration pages, and the API tests depend on the availability and behavior of the public JSONPlaceholder service. It is not a production application or a comprehensive test suite for a real authentication system.
