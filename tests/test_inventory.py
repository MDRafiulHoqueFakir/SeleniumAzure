import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Inventory")
class TestInventory:

    @allure.story("Logout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Perform logout"):
            inventory_page.logout()
            
        with allure.step("Verify redirection to login page"):
            WebDriverWait(driver, 30).until_not(EC.url_contains("inventory.html"))
            assert "saucedemo.com" in driver.current_url and "inventory.html" not in driver.current_url
            assert driver.find_element(*LoginPage.LOGIN_BUTTON).is_displayed()

    @allure.story("Sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_low_to_high(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Sort products by Price (low to high)"):
            inventory_page.sort_by("lohi")
            
        with allure.step("Verify sorting"):
            prices = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
            price_values = [float(price.text.replace("$", "")) for price in prices]
            assert price_values == sorted(price_values), "Prices are not sorted low to high"

    @allure.story("App State")
    @allure.severity(allure.severity_level.NORMAL)
    def test_reset_app_state(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Add item to cart"):
            inventory_page.add_item_to_cart("sauce-labs-backpack")
            assert inventory_page.get_cart_count() == 1
            
        with allure.step("Reset App State"):
            inventory_page.reset_app_state()
            driver.refresh()
            
        with allure.step("Verify cart is empty"):
            # Verify badge is not present or empty
            try:
                WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(InventoryPage.CART_BADGE))
            except:
                pass # If it's already gone or never there, that's fine, we check count next
            badges = driver.find_elements(*InventoryPage.CART_BADGE)
            assert len(badges) == 0 or not badges[0].is_displayed()

    @allure.story("Advanced: Network Interception")
    @allure.severity(allure.severity_level.NORMAL)
    def test_inventory_no_images(self, driver):
        # Only works with Chromium-based browsers (Chrome, Edge)
        if driver.name not in ["chrome", "MicrosoftEdge"]:
            pytest.skip("Network interception only supported on Chromium-based browsers")

        # Enable Network domain
        driver.execute_cdp_cmd("Network.enable", {})
        # Block images
        driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.jpg", "*.png", "*.jpeg", "*.gif"]})

        login_page = LoginPage(driver)
        
        with allure.step("Login with images blocked"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Verify page loads without images"):
            inventory_list = driver.find_element(By.CSS_SELECTOR, ".inventory_list")
            assert inventory_list.is_displayed()
            items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
            assert len(items) == 6
