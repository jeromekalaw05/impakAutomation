import logging
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(6)  # Adjust the order as needed
def test_add_group(driver):
    wait = WebDriverWait(driver, 20)

    try:
        wait.until(EC.element_to_be_clickable(Locators.SIDEBAR_GROUPS)).click()

        wait.until(EC.element_to_be_clickable(Locators.CREATE_GROUP_BUTTON)).click()

        group_name_input = wait.until(EC.presence_of_element_located(Locators.GROUP_NAME_INPUT_FIELD))
        group_name_input.send_keys(Locators.GROUP_NAME)

        wait.until(EC.visibility_of_element_located(Locators.GROUP_LEADER_DROPDOWN)).click()

        wait.until(EC.visibility_of_element_located(Locators.GROUP_LEADER_DROPDOWN_OPTION)).click()
        
        wait.until(EC.element_to_be_clickable(Locators.ADD_NEW_GROUP_BUTTON)).click()

        test_group = wait.until(EC.visibility_of_element_located(Locators.TEST_ADD_GROUP))
        assert test_group.is_displayed(), "Group is not added"

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure