import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Login")
class TestLogin:
    """
    Test suite for Login functionality.
    Covers positive, negative, and data-driven scenarios.
    """

    @allure.story("Positive Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, driver):
        """Verify that a valid user can login successfully."""
        login_page = LoginPage(driver)
        
        with allure.step("Open Login Page"):
            login_page.load()
            
        with allure.step("Login with valid credentials"):
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Verify redirection to inventory"):
            assert "inventory.html" in driver.current_url

    @allure.story("Negative Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_out_user(self, driver):
        """Verify error message for locked-out user."""
        login_page = LoginPage(driver)
        
        with allure.step("Open Login Page"):
            login_page.load()
            
        with allure.step("Login with locked out user"):
            login_page.login("locked_out_user", "secret_sauce")
            
        with allure.step("Verify error message"):
            assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_text()

    @allure.story("Negative Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_credentials(self, driver):
        """Verify error message for invalid password."""
        login_page = LoginPage(driver)
        
        with allure.step("Open Login Page"):
            login_page.load()
            
        with allure.step("Login with invalid password"):
            login_page.login("standard_user", "wrong_password")
            
        with allure.step("Verify error message"):
            assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_text()

    @allure.story("Negative Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_username(self, driver):
        """Verify error message for empty username."""
        login_page = LoginPage(driver)
        
        with allure.step("Open Login Page"):
            login_page.load()
            
        with allure.step("Login with empty username"):
            login_page.login("", "secret_sauce")
            
        with allure.step("Verify error message"):
            assert "Epic sadface: Username is required" in login_page.get_error_text()

    @allure.story("Negative Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_password(self, driver):
        """Verify error message for empty password."""
        login_page = LoginPage(driver)
        
        with allure.step("Open Login Page"):
            login_page.load()
            
        with allure.step("Login with empty password"):
            login_page.login("standard_user", "")
            
        with allure.step("Verify error message"):
            assert "Epic sadface: Password is required" in login_page.get_error_text()

    @allure.story("Advanced: Data-Driven Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password", [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce")
    ])
    def test_login_parametrized(self, driver, username, password):
        """Verify login functionality with multiple valid user accounts."""
        login_page = LoginPage(driver)
        
        with allure.step(f"Login with user: {username}"):
            login_page.load()
            login_page.login(username, password)
            
        with allure.step("Verify login success"):
            assert "inventory.html" in driver.current_url

if __name__ == '__main__':
    pytest.main([__file__])
