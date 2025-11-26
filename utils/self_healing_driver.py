from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SelfHealingDriver")

class SelfHealingDriver:
    """
    A wrapper around Selenium WebDriver that implements self-healing capabilities.
    If a locator fails, it attempts to find the element using alternative strategies.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: tuple) -> WebElement:
        """
        Attempts to find an element. If the primary locator fails, triggers self-healing.
        """
        strategy, value = locator
        try:
            return self.driver.find_element(strategy, value)
        except NoSuchElementException:
            logger.warning(f"Locator failed: {locator}. Attempting self-healing...")
            return self._heal_locator(locator)

    def _heal_locator(self, original_locator: tuple) -> WebElement:
        """
        Iterates through backup strategies to find the element.
        """
        strategy, value = original_locator
        
        # Define backup strategies based on the original strategy
        backup_strategies = []

        if strategy == By.CSS_SELECTOR:
            # If it's a complex CSS selector, try to extract ID or Class
            if "#" in value:
                # Extract ID: #some-id -> some-id
                potential_id = value.split("#")[-1].split(" ")[0].split(".")[0]
                backup_strategies.append((By.ID, potential_id))
            if "." in value:
                # Extract Class: .some-class -> some-class
                potential_class = value.split(".")[-1].split(" ")[0]
                backup_strategies.append((By.CLASS_NAME, potential_class))
        
        elif strategy == By.ID:
            # Try CSS selector with ID
            backup_strategies.append((By.CSS_SELECTOR, f"#{value}"))
            # Try XPath with ID
            backup_strategies.append((By.XPATH, f"//*[@id='{value}']"))

        # Generic backups (risky but worth a try if specific ones fail)
        # Try finding by text if the value looks like text (no special chars)
        if " " in value and not any(c in value for c in "[]#."):
             backup_strategies.append((By.XPATH, f"//*[contains(text(), '{value}')]"))

        # Execute backup strategies
        for backup_strategy, backup_value in backup_strategies:
            try:
                logger.info(f"Trying backup strategy: {backup_strategy}='{backup_value}'")
                element = self.driver.find_element(backup_strategy, backup_value)
                logger.info(f"Self-healing successful! Found element using: {backup_strategy}='{backup_value}'")
                return element
            except NoSuchElementException:
                continue

        # If all fail, raise the original exception
        logger.error(f"Self-healing failed for locator: {original_locator}")
        raise NoSuchElementException(f"Could not find element after self-healing attempts: {original_locator}")

    def __getattr__(self, name):
        """
        Delegate all other method calls to the original driver.
        """
        return getattr(self.driver, name)
