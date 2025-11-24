import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
import random
import string
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Checkout")
class TestCheckout:
    """
    Test suite for Checkout functionality.
    Includes dynamic data input and negative form validation.
    """

    @allure.story("Advanced: Dynamic Data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_dynamic_data(self, driver):
        """
        Verify checkout with randomly generated user data.
        Ensures application handles variable input correctly.
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        # Helper functions for random data
        def random_string(length=8):
            return ''.join(random.choices(string.ascii_letters, k=length))
            
        def random_digits(length=5):
            return ''.join(random.choices(string.digits, k=length))

        first_name = random_string()
        last_name = random_string()
        zip_code = random_digits()
        
        with allure.step("Login and go to checkout"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            inventory_page.go_to_cart()
            
        with allure.step(f"Checkout with dynamic data: {first_name} {last_name}, {zip_code}"):
            cart_page.checkout(first_name, last_name, zip_code)
            
        with allure.step("Verify checkout overview"):
            assert driver.find_element(*CartPage.FINISH_BUTTON).is_displayed()

    @allure.story("Negative Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_empty_firstname(self, driver):
        """Verify error message when First Name is empty."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login and go to checkout"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            inventory_page.go_to_cart()
            driver.find_element(*CartPage.CHECKOUT_BUTTON).click()
            
        with allure.step("Try to continue with empty first name"):
            driver.find_element(*CartPage.LAST_NAME_INPUT).send_keys("Doe")
            driver.find_element(*CartPage.POSTAL_CODE_INPUT).send_keys("12345")
            driver.find_element(*CartPage.CONTINUE_BUTTON).click()
            
        with allure.step("Verify error message"):
            assert "Error: First Name is required" in cart_page.get_checkout_error()

    @allure.story("Negative Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_empty_lastname(self, driver):
        """Verify error message when Last Name is empty."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login and go to checkout"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            inventory_page.go_to_cart()
            driver.find_element(*CartPage.CHECKOUT_BUTTON).click()
            
        with allure.step("Try to continue with empty last name"):
            driver.find_element(*CartPage.FIRST_NAME_INPUT).send_keys("John")
            driver.find_element(*CartPage.POSTAL_CODE_INPUT).send_keys("12345")
            driver.find_element(*CartPage.CONTINUE_BUTTON).click()
            
        with allure.step("Verify error message"):
            assert "Error: Last Name is required" in cart_page.get_checkout_error()

    @allure.story("Negative Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_empty_zip(self, driver):
        """Verify error message when Postal Code is empty."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login and go to checkout"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            inventory_page.go_to_cart()
            driver.find_element(*CartPage.CHECKOUT_BUTTON).click()
            
        with allure.step("Try to continue with empty zip code"):
            driver.find_element(*CartPage.FIRST_NAME_INPUT).send_keys("John")
            driver.find_element(*CartPage.LAST_NAME_INPUT).send_keys("Doe")
            driver.find_element(*CartPage.CONTINUE_BUTTON).click()
            
        with allure.step("Verify error message"):
            assert "Error: Postal Code is required" in cart_page.get_checkout_error()

if __name__ == '__main__':
    pytest.main([__file__])
