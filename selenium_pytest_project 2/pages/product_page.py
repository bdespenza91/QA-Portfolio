from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Rating stars — each star is a label or button indexed 1–5
    STAR_RATING = lambda self, stars: (
        By.XPATH,
        f"(//input[@name='rating' and @value='{stars}']/../label | //span[contains(@class,'star')][{stars}])"
    )
    FEEDBACK_TEXTAREA = (By.XPATH, "//textarea[@name='comment' or @placeholder]")
    SUBMIT_RATING_BUTTON = (By.XPATH, "//button[contains(text(),'Submit') and (ancestor::form[contains(@class,'rating')] or ancestor::section[contains(@class,'review')])]")
    RATING_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'submitted') or contains(text(),'Thank you') or contains(@class,'success')]")
    RATING_ERROR_MESSAGE = (By.XPATH, "//*[contains(@class,'error') or contains(text(),'cannot') or contains(text(),'Error')]")

    EDIT_RATING_BUTTON = (By.XPATH, "//button[contains(text(),'Edit')]")
    DELETE_RATING_BUTTON = (By.XPATH, "//button[contains(text(),'Delete') or contains(text(),'Remove')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(text(),'Confirm') or contains(text(),'Yes')]")

    DISPLAYED_RATING = (By.XPATH, "//div[contains(@class,'user-review') or contains(@class,'my-review')]")
    AVERAGE_RATING = (By.XPATH, "//*[contains(@class,'average') or contains(@class,'avg-rating')]")

    NOT_PURCHASED_ERROR = (By.XPATH, "//*[contains(text(),'purchase') or contains(text(),'buy') or contains(@class,'error')]")

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Add to Cart') or contains(text(),'Add to Bag')]")

    def click_star(self, stars: int):
        self.click(self.STAR_RATING(stars))

    def enter_feedback(self, text: str):
        self.type_text(self.FEEDBACK_TEXTAREA, text)

    def submit_rating(self):
        self.click(self.SUBMIT_RATING_BUTTON)

    def is_rating_submitted(self) -> bool:
        return self.is_visible(self.RATING_SUCCESS_MESSAGE)

    def get_rating_error(self) -> str:
        return self.get_text(self.RATING_ERROR_MESSAGE)

    def click_edit_rating(self):
        self.click(self.EDIT_RATING_BUTTON)

    def click_delete_rating(self):
        self.click(self.DELETE_RATING_BUTTON)

    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BUTTON)

    def is_rating_visible(self) -> bool:
        return self.is_visible(self.DISPLAYED_RATING)

    def get_average_rating_text(self) -> str:
        return self.get_text(self.AVERAGE_RATING)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
