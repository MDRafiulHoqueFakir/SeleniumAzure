import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@allure.feature("Self Healing")
class TestSelfHealing:

    @allure.story("Heuristic Locator Recovery")
    def test_broken_locator_recovery(self, driver):
        """
        Verify that the driver can find an element even if the primary locator is wrong,
        by using backup strategies (e.g. finding by ID extracted from CSS).
        """
        login_page = LoginPage(driver)
        login_page.load()
        
        # The actual ID is "user-name". We will try to find it using a broken CSS selector
        # that contains the ID but is syntactically wrong or just different, 
        # but our heuristic might pick up the ID part.
        # Actually, let's try a strategy that fails first, then falls back.
        
        # Strategy: CSS Selector that is incorrect but contains the ID.
        # Our SelfHealingDriver looks for '#' in CSS value to extract ID.
        # Let's say the dev changed the ID to 'user-name-new' but we still look for '#user-name'.
        # Wait, the logic is: if CSS fails, extract ID from the *locator string* and try finding by ID.
        # So if we look for "#user-name", and it fails (maybe because it's not an ID anymore but a class?), 
        # it will try By.ID "user-name".
        
        # Let's try a scenario: 
        # We want to find the login button. ID is "login-button".
        # Let's pretend we are looking for it by a complex CSS that fails, but we include the ID.
        # broken_locator = (By.CSS_SELECTOR, "div.login_container > form > #login-button") 
        # If the structure changed, this CSS might fail. But the ID "login-button" is still there.
        # The heuristic extracts "login-button" from "#login-button" and tries By.ID.
        
        broken_locator = (By.CSS_SELECTOR, "div.wrong_container > #login-button")
        
        # This should trigger self-healing
        element = login_page.driver.find_element(broken_locator)
        
        assert element.is_displayed()
        assert element.get_attribute("id") == "login-button"

if __name__ == '__main__':
    pytest.main([__file__])
