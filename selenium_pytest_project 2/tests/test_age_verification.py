"""
Test Suite: Age Verification for Alcohol
Test Design Techniques: BVA, EP, Error Guessing, Use Case Testing
"""
import pytest
from pages.store_page import StorePage
from pages.age_verification_page import AgeVerificationPage
from utils.constants import BASE_URL, ALCOHOL_URL, ALCOHOL_PRODUCT_NAME
from utils.helpers import dob_exactly_18, dob_under_18, dob_over_18


# ── Use Case Testing ──────────────────────────────────────────────────────────

def test_age_verification_modal_appears_on_alcohol_category(driver):
    """TC-1: Age verification modal appears when navigating to alcohol category."""
    store = StorePage(driver)
    store.open()
    store.click_alcohol_category()

    age_page = AgeVerificationPage(driver)
    assert age_page.is_modal_visible(), (
        "Expected age verification modal to appear when accessing the alcohol category"
    )


def test_age_verification_persists_within_session(driver):
    """TC-8: Modal does not reappear after age is verified in the same session."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    assert age_page.is_modal_visible(), "Pre-condition: modal should appear on first visit"

    age_page.enter_date_of_birth(dob_over_18())
    age_page.submit()

    # Navigate away and return
    driver.get(BASE_URL)
    driver.get(ALCOHOL_URL)

    assert not age_page.is_modal_visible(), (
        "Expected age verification modal NOT to reappear in the same session after verification"
    )


def test_age_verification_via_search(driver):
    """TC-9: Age verification modal appears when accessing an alcohol product via search."""
    store = StorePage(driver)
    store.open()
    store.search(ALCOHOL_PRODUCT_NAME)
    store.click_product(ALCOHOL_PRODUCT_NAME)

    age_page = AgeVerificationPage(driver)
    assert age_page.is_modal_visible(), (
        "Expected age verification modal when reaching alcohol product via search"
    )


def test_age_verification_via_direct_link(driver):
    """TC-10: Age verification modal appears when opening alcohol product URL directly."""
    driver.get(ALCOHOL_URL)

    age_page = AgeVerificationPage(driver)
    assert age_page.is_modal_visible(), (
        "Expected age verification modal when navigating directly to alcohol category URL"
    )


# ── Boundary Value Analysis ───────────────────────────────────────────────────

def test_access_granted_for_user_exactly_18(driver):
    """TC-2 (BVA): User who is exactly 18 years old is granted access."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    age_page.enter_date_of_birth(dob_exactly_18())
    age_page.submit()

    assert not age_page.is_access_denied(), (
        "Expected access to be granted for a user who is exactly 18 years old"
    )
    assert "Alcohol" in driver.current_url or not age_page.is_modal_visible(), (
        "Expected to remain on alcohol page after successful verification at exactly 18"
    )


def test_access_denied_for_user_just_below_18(driver):
    """TC-3 (BVA): User who is 17 years and 364 days old is denied access."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    age_page.enter_date_of_birth(dob_under_18())
    age_page.submit()

    assert age_page.is_access_denied() or age_page.is_on_homepage(BASE_URL), (
        "Expected access to be denied for a user just one day below 18 years old"
    )


# ── Equivalence Partitioning ──────────────────────────────────────────────────

@pytest.mark.parametrize("dob,should_allow", [
    (dob_over_18(17), False),   # EP: users under 18 (17 years old) → denied
    (dob_over_18(25), True),    # EP: users over 18 (25 years old) → granted
])
def test_access_by_age_group(driver, dob, should_allow):
    """TC-4 & TC-5 (EP): Verify access for users clearly above or below 18."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    age_page.enter_date_of_birth(dob)
    age_page.submit()

    if should_allow:
        assert not age_page.is_access_denied(), (
            f"Expected access to be GRANTED for DOB {dob}"
        )
    else:
        assert age_page.is_access_denied() or age_page.is_on_homepage(BASE_URL), (
            f"Expected access to be DENIED for DOB {dob}"
        )


# ── Error Guessing ────────────────────────────────────────────────────────────

def test_empty_date_of_birth_shows_error(driver):
    """TC-6 (Error Guessing): Empty DOB field shows 'Date of Birth is required' error."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    age_page.submit()

    error = age_page.get_error_message()
    assert error, "Expected an error message when submitting without a date of birth"
    assert "required" in error.lower() or "birth" in error.lower() or "date" in error.lower(), (
        f"Expected error to mention required date of birth, got: '{error}'"
    )


def test_invalid_date_format_shows_error(driver):
    """TC-7 (Error Guessing): Invalid date format is rejected with an error."""
    driver.get(ALCOHOL_URL)
    age_page = AgeVerificationPage(driver)

    age_page.enter_date_of_birth("99/99/9999")
    age_page.submit()

    error = age_page.get_error_message()
    assert error, "Expected an error message when submitting an invalid date format"
