from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    BasePage serves as the parent class for all page objects.
    It provides common methods and initializes the Selenium WebDriver.
    """

    def __init__(self, driver: WebDriver):
        """Initialize the BasePage with a Selenium WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def navigate(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Return the current page title."""
        return self.driver.title

    def get_url(self) -> str:
        """Return the current page URL."""
        return self.driver.current_url

    def find_element(self, locator: tuple):
        """Find a single element."""
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator: tuple):
        """Wait for an element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator: tuple, text: str):
        """Wait for an element to be visible, clear it, and enter text."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Wait for an element to be visible and return its text."""
        element = self.wait_for_element(locator)
        return element.text
