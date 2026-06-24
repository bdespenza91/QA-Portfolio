from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.constants import CART_URL


class CartPage(BasePage):
    CART_TOTAL = (By.XPATH, "//*[contains(@class,'subtotal') or contains(@class,'cart-total') or contains(text(),'Subtotal')]//following-sibling::* | //*[contains(@class,'total-price')]")
    SHIPPING_COST = (By.XPATH, "//*[contains(text(),'Shipping') or contains(text(),'Delivery')]//following-sibling::* | //*[contains(@class,'shipping')]")
    FREE_SHIPPING_LABEL = (By.XPATH, "//*[contains(text(),'Free') and (contains(text(),'Shipping') or contains(text(),'Delivery'))]")
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(),'empty') or contains(text(),'no items') or contains(@class,'empty')]")
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Checkout') or contains(text(),'Proceed')]")
    CHECKOUT_SHIPPING = (By.XPATH, "//*[contains(@class,'shipping') or contains(text(),'Shipping')]")

    PRODUCT_QUANTITY_INPUT = lambda self, name: (
        By.XPATH,
        f"//div[contains(@class,'cart-item') and .//*[contains(text(),'{name}')]]//input[@type='number']"
    )
    REMOVE_ITEM_BUTTON = lambda self, name: (
        By.XPATH,
        f"//div[contains(@class,'cart-item') and .//*[contains(text(),'{name}')]]//button[contains(text(),'Remove') or @aria-label='Remove']"
    )

    def open(self):
        self.driver.get(CART_URL)
        return self

    def get_shipping_cost_text(self) -> str:
        try:
            return self.get_text(self.SHIPPING_COST)
        except Exception:
            return ""

    def is_free_shipping(self) -> bool:
        try:
            text = self.get_shipping_cost_text().lower()
            return "free" in text or "0" in text or self.is_visible(self.FREE_SHIPPING_LABEL)
        except Exception:
            return self.is_visible(self.FREE_SHIPPING_LABEL)

    def get_cart_total_text(self) -> str:
        return self.get_text(self.CART_TOTAL)

    def is_empty_cart(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MESSAGE)

    def is_checkout_enabled(self) -> bool:
        try:
            btn = self.find(self.CHECKOUT_BUTTON)
            return btn.is_enabled()
        except Exception:
            return False

    def get_checkout_shipping_text(self) -> str:
        return self.get_text(self.CHECKOUT_SHIPPING)
