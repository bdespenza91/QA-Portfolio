import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.helpers import take_screenshot


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run tests headlessly")


@pytest.fixture
def driver(request):
    options = Options()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.nodeid.replace("/", "_").replace("::", "_")
            take_screenshot(driver, test_name)
