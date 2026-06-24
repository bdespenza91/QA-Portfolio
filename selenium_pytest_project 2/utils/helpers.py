import os
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def take_screenshot(driver, name: str) -> str:
    screenshots_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    path = os.path.join(screenshots_dir, f"{name}.png")
    driver.save_screenshot(path)
    return path


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_for_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def dob_exactly_18() -> str:
    """Return date of birth string for a user who turns 18 today."""
    today = date.today()
    dob = today.replace(year=today.year - 18)
    return dob.strftime("%Y-%m-%d")


def dob_under_18() -> str:
    """Return date of birth string for a user who is 17 years and 364 days old."""
    today = date.today()
    dob = today.replace(year=today.year - 18) + timedelta(days=1)
    return dob.strftime("%Y-%m-%d")


def dob_over_18(years: int = 25) -> str:
    """Return date of birth string for a user of a given age."""
    today = date.today()
    dob = today.replace(year=today.year - years)
    return dob.strftime("%Y-%m-%d")
