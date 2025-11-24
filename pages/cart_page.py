from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """
    Represents the Cart and Checkout pages.
    Contains methods for cart management and the checkout process.
    """

    # Locators
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    def get_item_name(self):
        """Return the name of the first item in the cart."""
        # Note: find_element returns the first match
        return self.get_text(self.ITEM_NAME)

    def get_item_price(self):
        """Return the price of the first item in the cart."""
        return self.get_text(self.ITEM_PRICE)

    def checkout(self, first_name, last_name, zip_code):
        """
        Perform the checkout flow:
        1. Click Checkout
        2. Fill user details
        3. Click Continue
        """
        self.click(self.CHECKOUT_BUTTON)
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)
        self.wait_for_element(self.FINISH_BUTTON)

    def finish_checkout(self):
        """Complete the order by clicking the Finish button."""
        self.click(self.FINISH_BUTTON)

    def get_complete_header(self):
        """Return the success message header after checkout."""
        return self.get_text(self.COMPLETE_HEADER)

    def remove_item(self, item_name_kebab_case):
        """Remove a specific item from the cart."""
        locator = (By.CSS_SELECTOR, f"[data-test='remove-{item_name_kebab_case}']")
        self.click(locator)

    def continue_shopping(self):
        """Navigate back to the inventory to continue shopping."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def get_checkout_error(self):
        """Return the error message displayed on the checkout page."""
        return self.get_text(self.ERROR_MESSAGE)
