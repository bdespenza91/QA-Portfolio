from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.constants import STORE_URL, ALCOHOL_URL


class StorePage(BasePage):
    ALCOHOL_CATEGORY_LINK = (By.XPATH, "//a[contains(text(),'Alcohol') or contains(@href,'Alcohol') or contains(@href,'alcohol')]")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search' or @placeholder='Search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and ancestor::form[.//input[@type='search']]]")
    PRODUCT_CARD = lambda self, name: (By.XPATH, f"//h2[contains(text(),'{name}')] | //p[contains(text(),'{name}')] | //*[contains(@class,'product-name') and contains(text(),'{name}')]")
    ADD_TO_CART_BTN = lambda self, name: (
        By.XPATH,
        f"//div[contains(@class,'product') and .//*[contains(text(),'{name}')]]//button[contains(text(),'Add')]"
    )

    def open(self):
        self.driver.get(STORE_URL)
        return self

    def open_alcohol(self):
        self.driver.get(ALCOHOL_URL)
        return self

    def click_alcohol_category(self):
        self.click(self.ALCOHOL_CATEGORY_LINK)

    def search(self, term: str):
        self.type_text(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def click_product(self, name: str):
        self.click(self.PRODUCT_CARD(name))

    def add_product_to_cart(self, name: str):
        self.click(self.ADD_TO_CART_BTN(name))
