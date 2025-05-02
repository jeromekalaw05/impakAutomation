import logging
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(4)
def test_add_employee(driver):

    wait = WebDriverWait(driver, 10)

    try:
        # Add employee process
        wait.until(EC.visibility_of_element_located(Locators.MODAL_CLOSE)).click()
        wait.until(EC.element_to_be_clickable(Locators.ADD_YOUR_EMPLOYEES)).click()
        # wait.until(EC.element_to_be_clickable(Locators.EMPLOYEE_MODULE)).click()
        # wait.until(EC.element_to_be_clickable(Locators.ADD_EMPLOYEE_BTN)).click()

        wait.until(EC.visibility_of_element_located(Locators.MODAL))

        email_input_field = wait.until(EC.visibility_of_element_located(Locators.EMPLOYEE_EMAIL_FIELD))
        assert email_input_field.is_displayed(), "email field is not visible"
        email_input_field.send_keys(Locators.EMPLOYEE_EMAIL_VALUE)

        fname_input_field = wait.until(EC.visibility_of_element_located(Locators.EMPLOYEE_FIRSTNAME_FIELD))
        assert fname_input_field.is_displayed(), "First name field is not visible"
        fname_input_field.send_keys(Locators.EMPLOYEE_FIRSTNAME_VALUE)

        lname_input_field = wait.until(EC.visibility_of_element_located(Locators.EMPLOYEE_LASTNAME_FIELD))
        assert lname_input_field.is_displayed(), "Last name field is not visible"
        lname_input_field.send_keys(Locators.EMPLOYEE_LASTNAME_VALUE)

        invite_button = wait.until(EC.element_to_be_clickable(Locators.EMPLOYEE_INVITE_BTN))
        assert invite_button.is_displayed(), "Invite button is displayed"
        assert invite_button.is_enabled(), "Invite button is clickable"
        invite_button.click()

        wait.until(EC.element_to_be_clickable(Locators.MODAL_CLOSE)).click()

    except TimeoutException as e:
        logging.exception(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure