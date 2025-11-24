# SeleniumAzure

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-green.svg)
![Pytest](https://img.shields.io/badge/pytest-7.0+-yellow.svg)
![Azure DevOps](https://img.shields.io/badge/azure--devops-pipeline-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**SeleniumAzure** is a comprehensive test automation framework engineered with **Python** and **Selenium WebDriver**. It is architected using the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and readability. This project is fully optimized for Continuous Integration/Continuous Deployment (CI/CD) pipelines using **Azure DevOps**.

---

## 📑 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Test Scenarios Covered](#-test-scenarios-covered)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running Tests](#-running-tests)
- [CI/CD Integration](#-cicd-integration)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🚀 Features

-   **Page Object Model (POM)**: Modular architecture separating test logic from UI interaction.
-   **Robust Error Handling**: Implements explicit waits and dynamic element location.
-   **Azure DevOps Ready**: Includes `azure-pipelines.yml` for seamless CI/CD integration.
-   **Pytest Framework**: Leverages fixtures, parametrization, and hooks for efficient testing.
-   **Cross-Browser Compatibility**: Designed to support Chrome, Firefox, and Edge.
-   **Detailed Reporting**: Generates HTML reports with screenshots on failure (configurable).

## 📂 Project Structure

```text
SeleniumAzure/
├── pages/                  # Page Object Model (POM) classes
│   ├── base_page.py        # Base class containing common WebDriver interactions
│   ├── login_page.py       # Encapsulates Login page elements and actions
│   ├── inventory_page.py   # Encapsulates Product Inventory page elements
│   └── cart_page.py        # Encapsulates Shopping Cart page elements
├── tests/                  # Pytest test scripts
│   ├── test_login.py       # Validates authentication flows (valid/invalid)
│   ├── test_inventory.py   # Validates product sorting, adding to cart
│   ├── test_cart.py        # Validates cart content and removal
│   ├── test_checkout.py    # Validates the checkout process
│   └── test_e2e.py         # Full End-to-End user journey (Login -> Checkout)
├── conftest.py             # Shared fixtures (Setup/Teardown, Browser Config)
├── requirements.txt        # Project dependencies
├── azure-pipelines.yml     # CI/CD Pipeline configuration
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## 🧪 Test Scenarios Covered

The framework currently covers the following critical business flows:

1.  **Authentication**:
    -   Successful login with valid credentials.
    -   Error handling for locked-out users and invalid credentials.
2.  **Inventory Management**:
    -   Sorting products (Name A-Z, Z-A, Price Low-High, High-Low).
    -   Adding items to the cart from the inventory page.
3.  **Shopping Cart**:
    -   Verifying items added to the cart.
    -   Removing items from the cart.
    -   Navigating to checkout.
4.  **Checkout Process**:
    -   Completing the checkout form with user details.
    -   Verifying order summary and total price.
    -   Completing the order successfully.
5.  **End-to-End (E2E)**:
    -   A complete user journey from Login to Order Completion.

## 🛠️ Prerequisites

Before running the tests, ensure you have the following installed:

-   **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
-   **Google Chrome**: [Download Chrome](https://www.google.com/chrome/)
-   **Git**: [Download Git](https://git-scm.com/downloads)

## 📦 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/MDRafiulHoqueFakir/SeleniumAzure.git
    cd SeleniumAzure
    ```

2.  **Create a virtual environment (Recommended):**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Running Tests

Execute the tests using the `pytest` command.

### Run All Tests
```bash
pytest
```

### Run Specific Test Module
```bash
pytest tests/test_login.py
```

### Generate HTML Report
```bash
pytest --html=report.html
```

### Run in Parallel (Speed up execution)
```bash
pytest -n auto
```

## 🔄 CI/CD Integration

This project is pre-configured for **Azure DevOps**. The `azure-pipelines.yml` file defines the build pipeline:

1.  **Trigger**: Pushes to the `main` branch.
2.  **VM Image**: Runs on `ubuntu-latest`.
3.  **Steps**:
    -   Installs Python 3.x.
    -   Installs dependencies from `requirements.txt`.
    -   Executes tests via `pytest`.
    -   Publishes test results to Azure DevOps.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the **MIT License**.

## 📞 Contact

**MDRafiulHoqueFakir**

-   **GitHub**: [MDRafiulHoqueFakir](https://github.com/MDRafiulHoqueFakir)
-   **Repository**: [SeleniumAzure](https://github.com/MDRafiulHoqueFakir/SeleniumAzure)
