from selenium.webdriver.common.by import By

class Locators: 
    # URLs
    IMPAK_URL = "https://impak.app/login"
    TEMP_MAIL_URL = "https://temp-mail.io/en"
    IMPAK_DASHBOARD_URL = "https://impak.app/dashboard"

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
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[contains(text(),'Whoops! Something went wrong.')]")

    # Default test values
    SIGNUP_FIRST_NAME_VALUE = "For"
    SIGNUP_LAST_NAME_VALUE = "Testing"
    SIGNUP_PASSWORD_VALUE = "Password123"

    # WORKSPACE = (By.XPATH, "//div[h1[contains(text(), 'Test Only')]]/ancestor::div[contains(@class, 'justify-between')]//a[contains(text(), 'Open')]")

    # CREATE WORKSPACE LOCATORS
    COMPANY_NAME_FIELD = (By.ID, "company")
    COMPANY_CREATE_BTN = (By.XPATH, "//button[normalize-space(text())='Create']")
    CHOOSE_WORKSPACE = (By.XPATH, "//a[contains(text(), 'Open')]")

    # ADD EMPLOYEE LOCATORS
    MODAL = (By.ID, "feedback-modal")
    MODAL_CLOSE = (By.XPATH, "//button[@class='text-slate-400  hover:text-slate-500' and .//div[text()='Close']]")
    SIDEBAR_EMPLOYEE = (By.XPATH, "//a[.//span[normalize-space(text())='Employees']]")
    EMPLOYEE_MODULE = (By.XPATH, "//a[@href='https://upup-tech.impak.app/employee' and .//span[normalize-space(text())='Employees']]")
    ADD_EMPLOYEE_BTN = (By.CSS_SELECTOR, "button.p-1.5.rounded.border.border-slate-200.shadow-sm.ml-2")
    EMPLOYEE_EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email'][wire\:model='invites.0.email']")
    EMPLOYEE_FIRSTNAME_FIELD = (By.CSS_SELECTOR, "input[type='text'][wire\:model='invites.0.first_name']")
    EMPLOYEE_LASTNAME_FIELD = (By.CSS_SELECTOR, "input[type='text'][wire\:model='invites.0.last_name']")
    EMPLOYEE_INVITE_BTN = (By.XPATH, "//button[@type='submit' and normalize-space(text())='Invite']")
    SUCCESS_ADD_MESSAGE = (By.XPATH, "//div[@id='swal2-title' and contains(text(), 'Employees invited!')]")

    # ADD EMPLOYEE LOCATORS IF NEW ACCOUNT
    ADD_YOUR_EMPLOYEES = (By.XPATH, "//div[@class='flex items-center' and .//h3[text()='Add your employees']]")

    # ADD EMPLOYEE VALUES
    EMPLOYEE_EMAIL_VALUE = "test@abc.com"
    EMPLOYEE_FIRSTNAME_VALUE = "Random"
    EMPLOYEE_LASTNAME_VALUE = "Testing"