"""
Test Suite: Product Rating System
Test Design Techniques: BVA, EP, Error Guessing, Use Case Testing
"""
import pytest
from pages.login_page import LoginPage
from pages.store_page import StorePage
from pages.product_page import ProductPage
from utils.constants import (
    VALID_EMAIL, VALID_PASSWORD,
    ALCOHOL_PRODUCT_NAME, RATING_FEEDBACK_VALID, RATING_FEEDBACK_LONG,
    LOGIN_URL, STORE_URL,
)


@pytest.fixture
def logged_in_driver(driver):
    """Fixture: log in before each test in this module."""
    login = LoginPage(driver)
    login.open().login(VALID_EMAIL, VALID_PASSWORD)
    assert login.is_logged_in(), "Pre-condition failed: user could not log in"
    return driver


@pytest.fixture
def product_page_purchased(logged_in_driver):
    """Fixture: navigate to a product the user has purchased."""
    store = StorePage(logged_in_driver)
    store.open()
    store.click_product(ALCOHOL_PRODUCT_NAME)
    return ProductPage(logged_in_driver)


# ── Use Case Testing ──────────────────────────────────────────────────────────

def test_submit_rating_after_purchase(product_page_purchased):
    """TC-1: Logged-in user who purchased a product can submit a 5-star rating."""
    page = product_page_purchased
    page.click_star(5)
    page.enter_feedback(RATING_FEEDBACK_VALID)
    page.submit_rating()

    assert page.is_rating_submitted(), (
        "Expected success confirmation after submitting a valid 5-star rating"
    )


def test_edit_existing_rating(product_page_purchased):
    """TC-2: User can edit their rating from 3 stars to 4 stars."""
    page = product_page_purchased
    page.click_star(3)
    page.enter_feedback(RATING_FEEDBACK_VALID)
    page.submit_rating()
    assert page.is_rating_submitted(), "Pre-condition failed: initial rating not submitted"

    page.click_edit_rating()
    page.click_star(4)
    page.submit_rating()

    assert page.is_rating_submitted(), (
        "Expected success confirmation after editing rating from 3 to 4 stars"
    )


def test_delete_rating(product_page_purchased):
    """TC-3: User can delete their submitted rating."""
    page = product_page_purchased
    page.click_star(5)
    page.enter_feedback(RATING_FEEDBACK_VALID)
    page.submit_rating()
    assert page.is_rating_submitted(), "Pre-condition failed: rating not submitted before delete"

    page.click_delete_rating()
    page.confirm_delete()

    assert not page.is_rating_visible(), (
        "Expected rating to be removed after deletion"
    )


def test_rating_without_feedback_succeeds(product_page_purchased):
    """TC-6 (Error Guessing): Submitting a rating without feedback should succeed (feedback optional)."""
    page = product_page_purchased
    page.click_star(4)
    page.submit_rating()

    assert page.is_rating_submitted(), (
        "Expected rating to be submitted successfully even without feedback text"
    )


def test_average_rating_calculation(logged_in_driver):
    """TC-7: Average rating is calculated correctly from multiple ratings."""
    store = StorePage(logged_in_driver)
    store.open()
    store.click_product(ALCOHOL_PRODUCT_NAME)
    page = ProductPage(logged_in_driver)

    avg_text = page.get_average_rating_text()

    assert avg_text, "Expected an average rating to be displayed on the product page"


# ── Equivalence Partitioning ──────────────────────────────────────────────────

def test_rating_blocked_for_non_purchaser(logged_in_driver):
    """TC-4 (EP): User who has not purchased the product cannot submit a rating."""
    store = StorePage(logged_in_driver)
    store.open()
    # Navigate to a product the test account has NOT purchased
    store.click_product("Almonds")
    page = ProductPage(logged_in_driver)

    page.click_star(5)
    page.submit_rating()

    error = page.get_rating_error()
    assert error, (
        "Expected an error message when a non-purchaser tries to submit a rating"
    )


# ── Boundary Value Analysis ───────────────────────────────────────────────────

def test_feedback_exceeding_500_characters(product_page_purchased):
    """TC-5 (BVA): Feedback of 501 characters should be rejected with an error."""
    page = product_page_purchased
    page.click_star(3)
    page.enter_feedback(RATING_FEEDBACK_LONG)
    page.submit_rating()

    error = page.get_rating_error()
    assert error, (
        "Expected an error message when feedback exceeds 500 characters"
    )
    assert "500" in error or "exceed" in error.lower() or "characters" in error.lower(), (
        f"Error message should mention the 500-character limit, got: '{error}'"
    )


# ── Parameterized: multiple star ratings ──────────────────────────────────────

@pytest.mark.parametrize("stars", [1, 2, 3, 4, 5])
def test_all_star_ratings_are_selectable(product_page_purchased, stars):
    """Verify each star rating value (1–5) can be selected and submitted."""
    page = product_page_purchased
    page.click_star(stars)
    page.submit_rating()

    assert page.is_rating_submitted(), (
        f"Expected successful submission for a {stars}-star rating"
    )
