import logging
import time
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(5)  # Adjust the order as needed
def test_add_department(driver):
    wait = WebDriverWait(driver, 20)

    try:
        wait.until(EC.visibility_of_element_located(Locators.ADD_YOUR_DEPT)).click()

        wait.until(EC.visibility_of_element_located(Locators.CREATE_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.MODAL))

        department_name_input = wait.until(EC.presence_of_element_located(Locators.DEPARTMENT_NAME_INPUT_FIELD))
        department_name_input.send_keys(Locators.DEPARTMENT_NAME)

        time.sleep(1)

        wait.until(EC.presence_of_element_located(Locators.DEPARTMENT_HEAD_DROPDOWN)).click()

        time.sleep(1)

        wait.until(EC.presence_of_element_located(Locators.DEPARTMENT_HEAD_DROPDOWN_OPTION)).click()

        time.sleep(2)

        wait.until(EC.visibility_of_element_located(Locators.ADD_NEW_DEPARTMENT_BUTTON)).click()

        testing_dept = wait.until(EC.presence_of_element_located(Locators.TEST_ADD_DEPT))
        assert testing_dept.is_displayed(), "Department is not added"

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure