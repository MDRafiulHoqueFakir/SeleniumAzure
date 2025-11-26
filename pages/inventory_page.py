from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class InventoryPage(BasePage):
    """
    Represents the Inventory (Product Listing) Page.
    Contains methods to interact with products, the cart, and the main menu.
    """

    # Locators
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")

    def add_item_to_cart(self, item_name_kebab_case):
        """
        Add a specific item to the cart using its kebab-case name.
        Example: 'sauce-labs-backpack'
        """
        locator = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{item_name_kebab_case}']")
        self.click(locator)

    def get_cart_count(self):
        """Return the number of items currently in the cart."""
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        """Navigate to the Cart page."""
        self.click(self.CART_LINK)

    def sort_by(self, option_value):
        """
        Sort the inventory items by the given option value.
        Options: 'az', 'za', 'lohi', 'hilo'
        """
        element = self.wait_for_element(self.SORT_CONTAINER)
        select = Select(element)
        select.select_by_value(option_value)

    def open_menu(self):
        """Open the side menu."""
        self.click(self.MENU_BUTTON)
        # Wait for menu to be visible (animation) and interactive
        # Using a locator that represents the open menu container is better, but waiting for a link to be clickable is good too.
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))

    def logout(self):
        """Perform the logout action via the side menu."""
        self.open_menu()
        self.click(self.LOGOUT_LINK)

    def reset_app_state(self):
        """Reset the application state (e.g., clear cart) via the side menu."""
        self.open_menu()
        self.click(self.RESET_LINK)
        # Wait for reset to likely happen
        import time
        time.sleep(1) 
        self.click(self.CLOSE_MENU_BUTTON)
