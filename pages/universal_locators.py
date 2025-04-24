from selenium.webdriver.common.by import By

class Locators:
    def __init__(self, driver):
        self.driver = driver

    # URLs
    IMPAK_URL = "https://impak.app/login"
    TEMP_MAIL_URL = "https://temp-mail.io/en"

    # SIGNUP LOCATORS
    SIGNUP_FIRST_NAME_INPUT = (By.ID, "first_name")
    SIGNUP_LAST_NAME_INPUT = (By.ID, "last_name")
    SIGNUP_EMAIL_INPUT = (By.ID, "email")
    SIGNUP_PASSWORD_INPUT = (By.ID, "password")
    SIGNUP_CONFIRM_PASSWORD_INPUT = (By.ID, "password_confirmation")
    SIGNUP_TERMS_CHECKBOX = (By.ID, "terms")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign Up')]")

    SIGNUP_LINK_BUTTON = (By.XPATH, "//a[text()='Sign Up']")
    LOGOUT_LINK_BUTTON = (By.XPATH, "//button[contains(text(), 'Log Out')]")

    TEMP_MAIL_EMAIL = (By.ID, "email")

    # LOGIN LOCATORS
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign in')]")

    # Default test values
    SIGNUP_FIRST_NAME_VALUE = "Test"
    SIGNUP_LAST_NAME_VALUE = "Name"
    SIGNUP_PASSWORD_VALUE = "Password123"
