from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """
    Represents the Login Page of the application.
    Contains locators and methods to interact with the login form.
    """
    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        """Navigate to the Login Page."""
        self.navigate(self.URL)

    def login(self, username, password):
        """Perform the login action with the given credentials."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        """Retrieve the text of the error message displayed on failure."""
        return self.get_text(self.ERROR_MESSAGE)
