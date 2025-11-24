import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("E2E Checkout")
class TestE2E:
    """
    End-to-End (E2E) test suite.
    Covers the complete user journey from login to purchase completion.
    """

    @allure.story("Purchase Flow")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase_flow(self, driver):
        """
        Execute a complete purchase flow:
        Login -> Add Item -> Cart -> Checkout -> Finish -> Verify
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # 1. Login Step
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")

        # 2. Add Item Step
        item_name = "Sauce Labs Backpack"
        item_price = "$29.99"
        
        with allure.step(f"Add {item_name} to cart"):
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            assert inventory_page.get_cart_count() == 1

        # 3. Go to Cart Step
        with allure.step("Navigate to cart"):
            inventory_page.go_to_cart()

        # 4. Verify Item in Cart Step
        with allure.step("Verify item name and price in cart"):
            assert cart_page.get_item_name() == item_name, f"Expected {item_name}, but got {cart_page.get_item_name()}"
            assert cart_page.get_item_price() == item_price, f"Expected {item_price}, but got {cart_page.get_item_price()}"

        # 5. Checkout Step
        with allure.step("Proceed to checkout"):
            cart_page.checkout("John", "Doe", "12345")

        # 6. Finish Step
        with allure.step("Finish checkout"):
            cart_page.finish_checkout()
            
        with allure.step("Verify order completion"):
            assert "Thank you for your order!" in cart_page.get_complete_header()
