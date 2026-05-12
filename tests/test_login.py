from selenium.webdriver.common.by import By


def test_login(driver):

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login_button.click()

    title = driver.find_element(By.CLASS_NAME, "title")

    assert title.text == "Products"


def test_product_verification(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    product = driver.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Backpack']"
    )

    assert product.is_displayed()
