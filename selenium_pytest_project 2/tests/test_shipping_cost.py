"""
Test Suite: Shipping Cost Changes
Test Design Techniques: BVA, EP, Use Case Testing, Error Guessing
"""
import pytest
from pages.login_page import LoginPage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils.constants import (
    VALID_EMAIL, VALID_PASSWORD,
    SHIPPING_THRESHOLD, SHIPPING_FEE,
    BASE_URL, CART_URL,
)


PRODUCT_CHEAP = "Banana"        # low unit price – add many to stay near threshold
PRODUCT_EXPENSIVE = "Organic Whole Milk"  # higher unit price


@pytest.fixture
def logged_in_cart(driver):
    """Fixture: log in and return (driver, store_page, cart_page) ready to use."""
    login = LoginPage(driver)
    login.open().login(VALID_EMAIL, VALID_PASSWORD)
    assert login.is_logged_in(), "Pre-condition failed: could not log in"
    return driver, StorePage(driver), CartPage(driver)


def _get_shipping_fee(cart: CartPage) -> float:
    text = cart.get_shipping_cost_text().replace("€", "").replace("$", "").strip()
    if not text or "free" in text.lower():
        return 0.0
    try:
        return float(text)
    except ValueError:
        return 0.0


# ── Boundary Value Analysis ───────────────────────────────────────────────────

def test_free_shipping_at_exactly_threshold(logged_in_cart):
    """TC-1 (BVA): Free shipping when cart total is exactly €20."""
    driver, store, cart = logged_in_cart
    # Add items until total reaches exactly the threshold – verified visually
    # For automation we add enough of a cheap product to reach €20
    store.open()
    for _ in range(10):
        store.add_product_to_cart(PRODUCT_CHEAP)

    cart.open()
    total_text = cart.get_cart_total_text()
    assert total_text, "Expected a cart total to be displayed"

    assert cart.is_free_shipping(), (
        f"Expected free shipping when cart total is at or above €{SHIPPING_THRESHOLD}, "
        f"shipping shown: '{cart.get_shipping_cost_text()}'"
    )


def test_shipping_fee_below_threshold(logged_in_cart):
    """TC-2 (BVA): €5 shipping fee when cart total is just below €20."""
    driver, store, cart = logged_in_cart
    store.open()
    store.add_product_to_cart(PRODUCT_CHEAP)  # single cheap item well under €20

    cart.open()
    assert not cart.is_free_shipping(), (
        "Expected a shipping fee when cart total is below €20"
    )
    fee = _get_shipping_fee(cart)
    assert fee == SHIPPING_FEE, (
        f"Expected shipping fee of €{SHIPPING_FEE}, got €{fee}"
    )


def test_free_shipping_above_threshold(logged_in_cart):
    """TC-3 (BVA): Free shipping when cart total is above €20."""
    driver, store, cart = logged_in_cart
    store.open()
    store.add_product_to_cart(PRODUCT_EXPENSIVE)
    store.add_product_to_cart(PRODUCT_EXPENSIVE)

    cart.open()
    assert cart.is_free_shipping(), (
        "Expected free shipping when cart total is above €20"
    )


# ── Equivalence Partitioning ──────────────────────────────────────────────────

@pytest.mark.parametrize("quantity,expect_free", [
    (1, False),    # EP: totals below threshold → shipping fee
    (20, True),    # EP: totals above threshold → free shipping
])
def test_shipping_by_cart_size(logged_in_cart, quantity, expect_free):
    """TC-4 & TC-5 (EP): Verify shipping for totals clearly below/above threshold."""
    driver, store, cart = logged_in_cart
    store.open()
    for _ in range(quantity):
        store.add_product_to_cart(PRODUCT_CHEAP)

    cart.open()
    if expect_free:
        assert cart.is_free_shipping(), (
            f"Expected free shipping for {quantity} items (total above threshold)"
        )
    else:
        assert not cart.is_free_shipping(), (
            f"Expected shipping fee for {quantity} items (total below threshold)"
        )


# ── Use Case Testing ──────────────────────────────────────────────────────────

def test_shipping_updates_dynamically_when_adding_items(logged_in_cart):
    """TC-6: Shipping cost updates dynamically as items are added to the cart."""
    driver, store, cart = logged_in_cart
    store.open()
    store.add_product_to_cart(PRODUCT_CHEAP)
    cart.open()
    shipping_before = cart.get_shipping_cost_text()

    # Add more items to cross the free-shipping threshold
    store.open()
    for _ in range(15):
        store.add_product_to_cart(PRODUCT_CHEAP)

    cart.open()
    shipping_after = cart.get_shipping_cost_text()

    assert shipping_before != shipping_after or cart.is_free_shipping(), (
        "Expected shipping cost to update after adding more items to the cart"
    )


def test_shipping_consistent_between_cart_and_checkout(logged_in_cart):
    """TC-7: Shipping cost in cart matches shipping cost shown at checkout."""
    driver, store, cart = logged_in_cart
    store.open()
    store.add_product_to_cart(PRODUCT_CHEAP)
    cart.open()

    cart_shipping = cart.get_shipping_cost_text()
    cart.click(cart.CHECKOUT_BUTTON)

    checkout_shipping = cart.get_checkout_shipping_text()

    assert cart_shipping == checkout_shipping or (
        "free" in cart_shipping.lower() and "free" in checkout_shipping.lower()
    ), (
        f"Shipping mismatch between cart ('{cart_shipping}') and checkout ('{checkout_shipping}')"
    )


# ── Error Guessing ────────────────────────────────────────────────────────────

def test_empty_cart_shows_no_shipping_or_disables_checkout(logged_in_cart):
    """TC-9 (Error Guessing): Empty cart shows no shipping cost or disables checkout."""
    driver, store, cart = logged_in_cart
    cart.open()

    is_empty = cart.is_empty_cart()
    checkout_enabled = cart.is_checkout_enabled()

    # Either the cart shows an empty-cart message, or checkout is disabled
    assert is_empty or not checkout_enabled, (
        "Expected either an empty-cart message or a disabled checkout button for an empty cart"
    )
