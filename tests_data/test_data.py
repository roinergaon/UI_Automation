# test_data.py

LOGIN_CREDENTIALS = {
    "username": "standard_user",
    "password": "secret_sauce"
}

INVALID_LOGIN_CREDENTIALS = {
    "invalid_username": "not_standard_user",
    "invalid_password": "secret",
    "empty_username": "",
    "empty_password": ""
}

EXPECTED_RESULTS = {
    "invalid_username_valid_password": "Username and password do not match any user in this service",
    "valid_username_invalid_password": "Username and password do not match any user in this service",
    "empty_username": "Username is required",
    "empty_password": "Username and password do not match any user in this service",
    "empty_username_password": "Epic sadface",
    "products_page_validation": "Products",
    "cart_page_validation": "Your Cart",
    "order_validation": "Thank you for your order!",
    "order_validation_fail_scenario": "Thank you"
}

PRODUCTS = {
    "backpack": "Sauce Labs Backpack",
    "bike_light": "Sauce Labs Bike Light",
    "bolt_tshirt": "Sauce Labs Bolt T-Shirt",
    "fleece_jacket": "Sauce Labs Fleece Jacket",
    "onesie": "Sauce Labs Onesie",
    "red_tshirt": "Test.allTheThings() T-Shirt (Red)"
}

INFORMATION_PAGE = {
    "first_name": "Roi",
    "last_name": "Ner Gaon",
    "postal_code": "7954187"
}

ERROR_MESSAGES = {
    "empty_first_name": "First Name is required",
    "empty_last_name": "Last Name is required",
    "empty_postal_code": "Postal Code is required",
    "empty_all_fields": "First Name is required"
}
