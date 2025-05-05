import logging
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.skip
@pytest.mark.order()
def test_login(driver):

    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located(Locators.SIDEBAR_SURVEYS)).click()
        wait.until(EC.visibility_of_element_located(Locators.SIDEBAR_ONGOING)).click()
        wait.until(EC.visibility_of_element_located(Locators.CREATE_SURVEY_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.SURVEY_OPTION)).click()
        wait.until(EC.visibility_of_element_located(Locators.SIDEBAR_ONGOING)).click()
        wait.until(EC.visibility_of_element_located(Locators.MODAL))
        wait.until(EC.visibility_of_element_located(Locators.MODAL_CLOSE)).click()
        wait.until(EC.visibility_of_element_located(Locators.ONBOARD_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.USE_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.SETUP_BTN)).click()
        
        survey_name = wait.until(EC.visibility_of_element_located(Locators.SURVEY_NAME))
        assert survey_name.is_enabled(), "Survey name field not working"
        survey_name.send_keys(Locators.SURVEY_NAME_VALUE)

        submission = wait.until(EC.visibility_of_element_located(Locators.SUBMISSION))
        submission.clear()
        assert submission.is_enabled(), "No of submission field not working"
        submission.send_keys(Locators.SUBMISSION_VALUE)

        wait.until(EC.visibility_of_element_located(Locators.SETUP_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.RESPONDENTS_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.TOGGLE_PUBLIC)).click()
        wait.until(EC.visibility_of_element_located(Locators.RESPONDENTS_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.PUBLISH_BTN)).click()
        wait.until(EC.visibility_of_element_located(Locators.PUBLISH_CONFIRM_BTN)).click()

        mark_as_done_btn = wait.until(EC.visibility_of_element_located(Locators.MARK_AS_DONE_BTN))
        assert mark_as_done_btn.is_displayed(), "Survey not created"

    except TimeoutException as e:
        logging.exception(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure