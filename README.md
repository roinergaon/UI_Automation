https://github.com/roinergaon/UI_Automation/assets/50953734/79e4d1a4-935a-4597-a022-b16274e59b8d

## 📖 Overview

This repository contains a comprehensive automated testing project built with python, pytest, Jenkins and Allure Reports. 
The project follows the Page Object Model (POM) design pattern for a modular and maintainable test suite.

## 📑 Technologies & Skill & Features
| Technologies      | Description |
| ----------- | ----------- |
| **Python:**      | The project is developed using Python |
| **Pytest:**   | Pytest is used as the testing framework, offering powerful test configuration options, parallel execution, and detailed reporting.        |
| **Selenium WebDriver:**   | The project includes Selenium WebDriver for automating browser interactions        |
| **Page Object Model (POM):**   | The project follows the POM design pattern, enhancing test maintainability and reusability by separating page elements and actions.        |
| **Allure Reports:**   | Test results are documented using Allure Reports, providing a clear and interactive visualization of test execution.        |
| **Jenkins:**   | Continuous integration and continuous delivery (CI/CD) platform for automated builds and deployments.        |

## 📊 Reports Examples
<p>
  <img src="ScreenShots/tc02_addTask1615288676297.jpg" width="40%" title="Example for screenshot on failure"  />
  <img src="ScreenShots/tc01_addTask1614893191281.jpg" width="40%" alt="Example for screenshot on failure" />
</p>

## 📁 Project Structure
```
│   log_info.log
│   utils.py
├───allure-reports
├───pageObjects
│   │   base_page.py
│   │   cart_page.py
│   │   customer_information_page.py
│   │   login_page.py
│   │   menu_page.py
│   │   order_completion_page.py
│   │   overview_page.py
│   │   products_page.py
│   │   single_product_page.py
│   │   __init__.py
│   │

├───tests
│   │   conftest.py
│   │   log_info.log
│   │   test_add_to_cart.py
│   │   test_buy_product.py
│   │   test_customer_information.py
│   │   test_login.py
│   │   test_order_completion.py
│   │   Test_products_overview.py
│   │   test_product_view.py
│   │   __init__.py
│
├───tests_data
│   │   test_data.py
│   
├───utils 
```
Roi Ner Gaon 








