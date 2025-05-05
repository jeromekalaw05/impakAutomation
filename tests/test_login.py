import logging
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(2)
def test_login(driver, temp_email_store):

    wait = WebDriverWait(driver, 10)

    try:
        # Use email from store
        temp_email = temp_email_store.get("email")
        assert temp_email is not None, "Temp email not found in store"

        # Login process
        login_email = wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL))
        assert login_email.is_displayed(), "Login email field is not visible"
        login_email.send_keys(temp_email)

        # Check if correct email inserted in the email field
        login_email_value = login_email.get_attribute("value")
        assert temp_email == login_email_value, "Email do not match"

        login_password = wait.until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD))
        assert login_password.is_displayed(), "Login password field is not visible"
        login_password.send_keys(Locators.SIGNUP_PASSWORD_VALUE)

        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Login button is not visible"
        assert login_button.is_enabled(), "Login button is not clickable"
        login_button.click()

        # Check if login failed and error message appeared
        if driver.current_url != Locators.IMPAK_DASHBOARD_URL:
            # If not redirected to dashboard, check for error message
            error_message = wait.until(EC.visibility_of_element_located(Locators.LOGIN_ERROR_MESSAGE))
            assert error_message.is_displayed(), "Error message not displayed for error occured"
            logging.error("Login failed error occured while logging in.")
        else:
            # If redirected to dashboard, successful login
            assert driver.current_url.startswith(Locators.IMPAK_DASHBOARD_URL), "Login successful"

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure