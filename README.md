# Selenium Automation with Python

## Overview
This project demonstrates automated web testing using **Selenium** with **Python**. It covers basic Python concepts and web automation techniques to interact with web elements, fill forms, click buttons, and validate page content.

## Prerequisites

### Software Requirements
- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- A web browser (Chrome, Firefox, or Edge)
- WebDriver for your chosen browser

### Python Basics Covered
- **Variables and Data Types**: Storing and managing test data
- **Functions**: Reusable code blocks for common automation tasks
- **Loops**: Iterating through multiple elements or test cases
- **Conditionals**: Making decisions based on element states
- **Exception Handling**: Managing errors gracefully during automation
- **Classes and Objects**: Organizing test code into reusable components
- **Modules and Imports**: Using Selenium and other libraries

## Installation

### Step 1: Clone or Navigate to Project
```bash
cd selenium_projects
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install selenium
pip install webdriver-manager  # Automatically manages WebDriver versions
```

### Step 4: Download WebDriver
The WebDriver should match your browser version. Options:
- **Chrome**: Download from [ChromeDriver](https://chromedriver.chromium.org/)
- **Firefox**: Download from [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Edge**: Download from [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Or use `webdriver-manager` to handle this automatically:
```bash
pip install webdriver-manager
```

## Basic Selenium Concepts

### 1. Importing Selenium
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

### 2. Creating a WebDriver Instance
```python
# Using webdriver-manager (recommended)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Or manually specify driver path
driver = webdriver.Chrome('./chromedriver')
```

### 3. Navigating to a Website
```python
driver.get("https://www.example.com")
```

### 4. Finding Elements
```python
# By ID
element = driver.find_element(By.ID, "element_id")

# By Name
element = driver.find_element(By.NAME, "element_name")

# By Class Name
element = driver.find_element(By.CLASS_NAME, "class_name")

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "css_selector")

# By XPath
element = driver.find_element(By.XPATH, "//xpath/expression")

# Find multiple elements
elements = driver.find_elements(By.TAG_NAME, "a")
```

### 5. Interacting with Elements
```python
# Click an element
element.click()

# Send text to input field
input_field = driver.find_element(By.ID, "search")
input_field.send_keys("search term")

# Clear text
input_field.clear()

# Get element text
text = element.text

# Get attribute value
href = element.get_attribute("href")
```

### 6. Waiting for Elements
```python
# Implicit Wait (applies to all elements)
driver.implicitly_wait(10)

# Explicit Wait (specific condition)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, "button_id")))
```

### 7. Closing the Browser
```python
driver.quit()  # Closes all windows
driver.close()  # Closes current window
```

## Project Structure

```
selenium_projects/
├── README.md              # This file
├── selm1.py              # Main selenium test script
├── syncrns.py            # Synchronization and waits example
└── requirements.txt      # Python dependencies (optional)
```

## File Descriptions

### `selm1.py`
Contains basic selenium automation examples:
- Opening websites
- Finding and interacting with elements
- Form filling and submission
- Assertion and validation

### `syncrns.py`
Demonstrates synchronization techniques:
- Implicit waits
- Explicit waits
- Expected conditions
- Handling dynamic content

## Running the Tests

### Run a Single Test File
```bash
python selm1.py
```

### Run with Python Directly
```bash
python -m selm1
```

## Example: Simple Login Test

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to website
    driver.get("https://example.com/login")
    
    # Wait and find username field
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Enter credentials
    username.send_keys("testuser@example.com")
    password = driver.find_element(By.ID, "password")
    password.send_keys("password123")
    
    # Click login button
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    
    # Wait for dashboard to load
    dashboard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
    )
    
    print("Login successful!")
    
finally:
    driver.quit()
```

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **WebDriver not found** | Install `webdriver-manager` or manually download the driver |
| **Element not found** | Use explicit waits or check if element is in iframe |
| **Stale element reference** | Re-find the element before interacting |
| **Timeout errors** | Increase wait time or check element selector |
| **Permission denied** | Ensure WebDriver file has execute permissions |

## Best Practices

1. **Use Explicit Waits**: Instead of `time.sleep()`, use `WebDriverWait` with expected conditions
2. **Use Page Object Model**: Organize code into page classes for maintainability
3. **Handle Exceptions**: Always use try-finally blocks to ensure `driver.quit()` is called
4. **Use Descriptive Selectors**: Prefer stable selectors (ID, Name) over brittle ones (CSS index)
5. **Avoid Hard Waits**: Use `WebDriverWait` instead of `time.sleep()`
6. **Log Actions**: Add print statements for debugging

## Additional Resources

- [Selenium Official Documentation](https://www.selenium.dev/documentation/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [WebDriver Manager GitHub](https://github.com/SergeyPirogov/webdriver_manager)
- [Python Official Documentation](https://docs.python.org/3/)

## License
This project is open source and available under the MIT License.

## Author
Generated for automation learning and testing purposes.

---

**Last Updated**: 2026-08-17
