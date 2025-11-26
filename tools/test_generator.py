import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.self_healing_driver import SelfHealingDriver

def generate_tests():
    """
    Crawls the application and generates a test file.
    """
    print("Starting Test Generator...")
    
    # Setup Driver
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Run headless for generation
    options.add_argument("--disable-gpu")
    original_driver = webdriver.Chrome(service=service, options=options)
    driver = SelfHealingDriver(original_driver)
    
    generated_test_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test_generated.py')
    
    try:
        # 1. Login
        print("Navigating to Login Page...")
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element((By.ID, "user-name")).send_keys("standard_user")
        driver.find_element((By.ID, "password")).send_keys("secret_sauce")
        driver.find_element((By.ID, "login-button")).click()
        
        print("Login successful. Scanning Inventory Page...")
        time.sleep(2) # Wait for load
        
        # 2. Scan for elements
        # Find all "Add to cart" buttons
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        # Find all Item links
        item_links = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        
        print(f"Found {len(add_to_cart_buttons)} Add to Cart buttons.")
        print(f"Found {len(item_links)} Item links.")
        
        # 3. Generate Test File
        with open(generated_test_path, "w") as f:
            f.write("import sys\n")
            f.write("import os\n")
            f.write("sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n")
            f.write("import pytest\n")
            f.write("import allure\n")
            f.write("from selenium.webdriver.common.by import By\n")
            f.write("from pages.login_page import LoginPage\n\n")
            
            f.write("@allure.feature('Generated Tests')\n")
            f.write("class TestGenerated:\n\n")
            
            f.write("    @pytest.fixture(autouse=True)\n")
            f.write("    def setup(self, driver):\n")
            f.write("        self.login_page = LoginPage(driver)\n")
            f.write("        self.login_page.load()\n")
            f.write("        self.login_page.login('standard_user', 'secret_sauce')\n\n")
            
            # Generate test for each item link
            for i, link in enumerate(item_links):
                item_name = link.text
                # Sanitize name for function name
                safe_name = "".join(c for c in item_name if c.isalnum() or c == '_').lower()
                
                f.write(f"    @allure.story('Verify Item Visibility')\n")
                f.write(f"    def test_item_visibility_{safe_name}_{i}(self, driver):\n")
                f.write(f"        \"\"\"Verify that '{item_name}' is displayed.\"\"\"\n")
                f.write(f"        item = driver.find_element(By.XPATH, \"//div[text()='{item_name}']\")\n")
                f.write(f"        assert item.is_displayed()\n\n")

            # Generate test for cart buttons
            if add_to_cart_buttons:
                 f.write(f"    @allure.story('Verify Add to Cart Buttons')\n")
                 f.write(f"    def test_add_to_cart_buttons_exist(self, driver):\n")
                 f.write(f"        \"\"\"Verify that at least one Add to Cart button exists.\"\"\"\n")
                 f.write(f"        buttons = driver.find_elements(By.XPATH, \"//button[contains(text(), 'Add to cart')]\")\n")
                 f.write(f"        assert len(buttons) > 0\n\n")

            f.write("if __name__ == '__main__':\n")
            f.write("    pytest.main([__file__])\n")
            
        print(f"Test file generated at: {generated_test_path}")
        
    except Exception as e:
        print(f"Error during generation: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    generate_tests()
