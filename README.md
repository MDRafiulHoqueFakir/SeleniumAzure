# SeleniumAzure

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-green.svg)
![Pytest](https://img.shields.io/badge/pytest-7.0+-yellow.svg)
![Azure DevOps](https://img.shields.io/badge/azure--devops-pipeline-blue)

**SeleniumAzure** is a robust test automation framework built with Python and Selenium WebDriver, designed for seamless integration with Azure DevOps pipelines. It implements the Page Object Model (POM) design pattern to ensure maintainability, scalability, and readability of test scripts.

## 🚀 Features

-   **Page Object Model (POM)**: Separates page navigation and interaction logic from test scripts.
-   **Azure DevOps Integration**: Ready-to-use `azure-pipelines.yml` for CI/CD.
-   **Pytest Framework**: Utilizes powerful fixtures and plugins for efficient testing.
-   **Cross-Browser Support**: Compatible with Chrome, Firefox, and Edge (configurable).
-   **Reporting**: Generates HTML reports for test execution results.

## 📂 Project Structure

```text
SeleniumAzure/
├── pages/                  # Page Object Model (POM) classes
│   ├── base_page.py        # Base class with common WebDriver methods
│   ├── login_page.py       # Page object for Login functionality
│   ├── inventory_page.py   # Page object for Inventory/Product page
│   └── cart_page.py        # Page object for Cart functionality
├── tests/                  # Pytest test cases
│   ├── test_login.py       # Tests for user authentication
│   ├── test_inventory.py   # Tests for product browsing and sorting
│   ├── test_cart.py        # Tests for cart operations
│   ├── test_checkout.py    # Tests for checkout flow
│   └── test_e2e.py         # End-to-End user journey tests
├── conftest.py             # Pytest configuration and shared fixtures
├── requirements.txt        # Python dependencies
├── azure-pipelines.yml     # Azure DevOps pipeline configuration
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## 🛠️ Prerequisites

-   **Python 3.8+**: Ensure Python is installed and added to your PATH.
-   **Google Chrome**: The tests are configured to run on Chrome by default.

## 📦 Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd SeleniumAzure
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_login.py
```

### Run with HTML Report
```bash
pytest --html=report.html
```

### Run in Parallel
```bash
pytest -n auto
```

## 🔄 CI/CD Pipeline

The project includes an `azure-pipelines.yml` file configured for Azure DevOps. It handles:
1.  Installing Python and dependencies.
2.  Running tests using `pytest`.
3.  Publishing test results and artifacts.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.
