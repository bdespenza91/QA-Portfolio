from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.constants import LOGIN_URL


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(),'Login')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout') or contains(text(),'Sign out')]")
    USER_MENU = (By.XPATH, "//span[contains(@class,'user') or contains(@class,'avatar')]")

    def open(self):
        self.driver.get(LOGIN_URL)
        return self

    def login(self, email: str, password: str):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return "auth" not in self.get_current_url()
