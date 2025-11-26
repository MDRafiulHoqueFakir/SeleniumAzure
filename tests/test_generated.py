import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@allure.feature('Generated Tests')
class TestGenerated:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.login_page.load()
        self.login_page.login('standard_user', 'secret_sauce')

    @allure.story('Verify Item Visibility')
    def test_item_visibility_saucelabsbackpack_0(self, driver):
        """Verify that 'Sauce Labs Backpack' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
        assert item.is_displayed()

    @allure.story('Verify Item Visibility')
    def test_item_visibility_saucelabsbikelight_1(self, driver):
        """Verify that 'Sauce Labs Bike Light' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']")
        assert item.is_displayed()

    @allure.story('Verify Item Visibility')
    def test_item_visibility_saucelabsbolttshirt_2(self, driver):
        """Verify that 'Sauce Labs Bolt T-Shirt' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")
        assert item.is_displayed()

    @allure.story('Verify Item Visibility')
    def test_item_visibility_saucelabsfleecejacket_3(self, driver):
        """Verify that 'Sauce Labs Fleece Jacket' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
        assert item.is_displayed()

    @allure.story('Verify Item Visibility')
    def test_item_visibility_saucelabsonesie_4(self, driver):
        """Verify that 'Sauce Labs Onesie' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']")
        assert item.is_displayed()

    @allure.story('Verify Item Visibility')
    def test_item_visibility_testallthethingstshirtred_5(self, driver):
        """Verify that 'Test.allTheThings() T-Shirt (Red)' is displayed."""
        item = driver.find_element(By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")
        assert item.is_displayed()

    @allure.story('Verify Add to Cart Buttons')
    def test_add_to_cart_buttons_exist(self, driver):
        """Verify that at least one Add to Cart button exists."""
        buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        assert len(buttons) > 0

if __name__ == '__main__':
    pytest.main([__file__])
