from selenium.webdriver.common.by import By
import time


def test_register_user(driver):

    driver.get("https://automationexercise.com/")

    assert driver.find_element(By.TAG_NAME, "body").is_displayed()

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    signup_text = driver.find_element(
        By.XPATH,
        "//h2[text()='New User Signup!']"
    )

    assert signup_text.is_displayed()

    driver.find_element(By.NAME, "name").send_keys("Barry Test")

    email = f"barrytest{int(time.time())}@gmail.com"

    driver.find_element(
        By.XPATH,
        "//input[@data-qa='signup-email']"
    ).send_keys(email)

    driver.find_element(
        By.XPATH,
        "//button[@data-qa='signup-button']"
    ).click()

    account_info = driver.find_element(
        By.XPATH,
        "//b[text()='Enter Account Information']"
    )

    assert account_info.is_displayed()

    driver.find_element(By.ID, "id_gender1").click()

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1995")

    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    driver.find_element(By.ID, "first_name").send_keys("Barry")
    driver.find_element(By.ID, "last_name").send_keys("Despenza")
    driver.find_element(By.ID, "company").send_keys("QA Portfolio")

    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "address2").send_keys("Berlin")

    driver.find_element(By.ID, "country").send_keys("United States")

    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")

    driver.find_element(By.ID, "mobile_number").send_keys("123456789")

    driver.find_element(
        By.XPATH,
        "//button[@data-qa='create-account']"
    ).click()

    created = driver.find_element(
        By.XPATH,
        "//b[text()='Account Created!']"
    )

    assert created.is_displayed()

    driver.find_element(
        By.XPATH,
        "//a[@data-qa='continue-button']"
    ).click()

    logged_in = driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )

    assert logged_in.is_displayed()

    driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Delete Account')]"
    ).click()

    deleted = driver.find_element(
        By.XPATH,
        "//b[text()='Account Deleted!']"
    )

    assert deleted.is_displayed()
