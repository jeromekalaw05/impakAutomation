import logging
import random
import string
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_company_name():
    prefix = "Test"
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}_{suffix}"

@pytest.mark.order(3)
def test_create_workspace(driver):

    wait = WebDriverWait(driver, 10)

    random_company_name = generate_random_company_name()
    logging.info(f"Generated Company Name: {random_company_name}")

    try:
        # Add employee process
        company_name_field = wait.until(EC.visibility_of_element_located(Locators.COMPANY_NAME_FIELD))
        assert company_name_field.is_displayed(), "Company name field not displayed"
        company_name_field.send_keys(random_company_name)

        create_btn = wait.until(EC.visibility_of_element_located(Locators.COMPANY_CREATE_BTN))
        assert create_btn.is_enabled(), "Create button not clickable"
        create_btn.click()

        choose_workspace = wait.until(EC.visibility_of_element_located(Locators.CHOOSE_WORKSPACE))
        assert choose_workspace.is_displayed(), "Open button not displayed"
        assert choose_workspace.is_enabled(), "Open button not clickable"
        choose_workspace.click()

    except TimeoutException as e:
        logging.exception(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure