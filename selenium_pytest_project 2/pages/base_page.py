from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator) -> bool:
        try:
            return self.find_visible(locator).is_displayed()
        except Exception:
            return False

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text.strip()

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text: str):
        element = self.find_clickable(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self) -> str:
        return self.driver.current_url
