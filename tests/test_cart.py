import pytest
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Cart")
class TestCart:
    """
    Test suite for Cart functionality.
    Includes item removal, continuing shopping, and UI layout verification.
    """

    @allure.story("Cart Management")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_item_from_cart(self, driver):
        """Verify that an item can be removed from the cart."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Add item to cart"):
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            
        with allure.step("Navigate to cart"):
            inventory_page.go_to_cart()
            
        with allure.step("Remove item from cart"):
            cart_page.remove_item("sauce-labs-backpack")
            
        with allure.step("Verify cart is empty"):
            cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
            assert len(cart_items) == 0

    @allure.story("Cart Management")
    @allure.severity(allure.severity_level.NORMAL)
    def test_continue_shopping(self, driver):
        """Verify that 'Continue Shopping' redirects back to inventory."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Navigate to cart"):
            inventory_page.go_to_cart()
            
        with allure.step("Click Continue Shopping"):
            cart_page.continue_shopping()
            
        with allure.step("Verify redirection to inventory"):
            assert "inventory.html" in driver.current_url

    @allure.story("Advanced: UI Layout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_layout(self, driver):
        """
        Verify the presence and text of key elements on the cart page.
        Ensures UI structure is correct (Title, Headers, Buttons).
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        with allure.step("Login and go to cart"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            inventory_page.go_to_cart()
            
        with allure.step("Verify UI Layout"):
            # Verify page title
            assert driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
            # Verify column headers
            assert driver.find_element(By.CSS_SELECTOR, ".cart_quantity_label").text == "QTY"
            assert driver.find_element(By.CSS_SELECTOR, ".cart_desc_label").text == "Description"
            # Verify buttons exist
            assert driver.find_element(*CartPage.CONTINUE_SHOPPING_BUTTON).is_displayed()
            assert driver.find_element(*CartPage.CHECKOUT_BUTTON).is_displayed()
