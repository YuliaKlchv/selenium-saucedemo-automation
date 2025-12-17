from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)

    # ENTER CREDENTIALS
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # ASSERT LOGIN SUCCESS
    assert "inventory.html" in driver.current_url, "Login failed"
    print("Login automation test passed successfully.")

# RUN TEST
driver = webdriver.Chrome()
test_login(driver)
driver.quit()
