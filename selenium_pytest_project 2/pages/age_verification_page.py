from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AgeVerificationPage(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class,'modal') or contains(@class,'age') or contains(@role,'dialog')]")
    DOB_INPUT = (By.XPATH, "//input[@type='date' or @name='dob' or @name='birthdate' or @placeholder]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' or contains(text(),'Verify') or contains(text(),'Enter') or contains(text(),'Confirm')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(@class,'error') or contains(text(),'required') or contains(text(),'invalid') or contains(text(),'denied')]")
    ACCESS_DENIED_MESSAGE = (By.XPATH, "//*[contains(text(),'not allowed') or contains(text(),'18') or contains(text(),'denied') or contains(text(),'redirect')]")

    def is_modal_visible(self) -> bool:
        return self.is_visible(self.MODAL)

    def enter_date_of_birth(self, dob: str):
        """Accept dob in YYYY-MM-DD format."""
        self.type_text(self.DOB_INPUT, dob)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_access_denied(self) -> bool:
        return self.is_visible(self.ACCESS_DENIED_MESSAGE)

    def is_on_homepage(self, base_url: str) -> bool:
        url = self.get_current_url()
        return url.rstrip("/") == base_url.rstrip("/") or "store" not in url
