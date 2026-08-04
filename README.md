# AI-Augmented Test Automation

UI, API, and visual regression test suites built in Python with Playwright and Selenium, integrating AI-powered testing tools.

## Tech Stack

- **Playwright** (Python) — UI test automation
- **pytest** — test runner and fixtures
- **Applitools Eyes** — AI-powered visual regression validation *(integration in progress)*
- **Postman AI (Postbot)** — AI-assisted API test generation *(collection in progress)*
- **Allure** — test execution reporting
- **Page Object Model (POM)** — test architecture pattern
- **GitHub Actions** — CI pipeline

## Project Structure

```
├── tests/
│   ├── ui/            # Playwright UI tests
│   └── api/           # API tests (requests + Postbot-generated assertions)
├── pages/             # Page Object Model classes
├── utils/             # Helpers and configuration
├── .github/workflows/ # CI pipeline
├── conftest.py        # pytest fixtures
└── requirements.txt
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium

# 4. Run tests
pytest tests/ -v

# 5. Run with Allure reporting
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Test Coverage

**UI tests** (Playwright) — run against [the-internet.herokuapp.com](https://the-internet.herokuapp.com), a public app built for test automation practice:
- Login: valid and invalid credentials, error message validation
- Dynamic content loading and waits
- Form interactions

**API tests** — run against [reqres.in](https://reqres.in) public REST API:
- CRUD operations (GET, POST, PUT, DELETE)
- Status code and response schema validation

## Roadmap

- [x] Playwright UI suite with POM structure
- [x] API test suite with pytest
- [x] Allure reporting
- [x] GitHub Actions CI
- [ ] Applitools Eyes visual regression suite
- [ ] Postman collection with Postbot-generated tests (exported to repo)
- [ ] Cross-browser matrix (Chromium, Firefox, WebKit)

## Author

Iuliia Ubushieva — QA Engineer
[LinkedIn](https://www.linkedin.com/in/iuliiaubushieva/)
