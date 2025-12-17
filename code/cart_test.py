from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_cart_with_items(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    # LOGIN
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # ADD PRODUCT TO CART
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    # GO TO CART
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # VERIFY CART ITEMS
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "No items found in the cart."
    print(f"Found {len(cart_items)} item(s) in the cart.")

    for item in cart_items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert name != "", "Item name is missing."
        assert price != "", "Item price is missing."

        print(f"Item name: {name}, price: {price}")

    print("Cart test passed successfully.")

# RUN TEST
driver = webdriver.Chrome()
test_cart_with_items(driver)
driver.quit()
