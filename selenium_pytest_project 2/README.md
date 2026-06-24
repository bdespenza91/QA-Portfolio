# Selenium Pytest Project — GroceryMate

Automated test suite for [grocerymate.masterschool.com](https://grocerymate.masterschool.com) using Selenium WebDriver and pytest, following the Page Object Model pattern.

## Project Structure

```
selenium_pytest_project/
├── pages/                    # Page Object Model classes
│   ├── base_page.py          # Shared helper methods (wait, click, find)
│   ├── login_page.py         # Login page interactions
│   ├── store_page.py         # Store navigation, search, add to cart
│   ├── product_page.py       # Product detail, star rating, feedback
│   ├── age_verification_page.py  # Age verification modal
│   └── cart_page.py          # Shopping cart and shipping cost
├── utils/
│   ├── constants.py          # URLs, credentials, thresholds
│   └── helpers.py            # DOB helpers, screenshot utility
├── tests/
│   ├── conftest.py           # WebDriver fixture, auto-screenshot on failure
│   ├── test_product_rating.py    # 9 tests: TC-1 through TC-7 + parametrized
│   ├── test_age_verification.py  # 9 tests: TC-1 through TC-10 + parametrized
│   └── test_shipping_cost.py     # 8 tests: TC-1 through TC-9 + parametrized
├── screenshots/              # Auto-saved on test failure
├── reports/                  # HTML report output
├── pytest.ini                # Pytest config
└── requirements.txt          # Dependencies
```

## Setup

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests and generate HTML report
pytest

# Run headlessly
pytest --headless

# Run a single suite
pytest tests/test_age_verification.py

# View report
open reports/report.html
```

## Test Coverage

| Suite | Techniques | Tests |
|---|---|---|
| Product Rating System | Use Case, BVA, EP, Error Guessing | 9 |
| Age Verification for Alcohol | Use Case, BVA, EP, Error Guessing | 9 |
| Shipping Cost Changes | BVA, EP, Use Case, Error Guessing | 8 |
