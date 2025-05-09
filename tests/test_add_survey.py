import logging
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(7)
def test_add_survey(driver):

    wait = WebDriverWait(driver, 20)

    try:
        survey = driver.find_element(*Locators.SIDEBAR_SURVEYS)
        survey.click()
        # wait.until(EC.element_to_be_clickable(Locators.SIDEBAR_SURVEYS)).click()

        wait.until(EC.visibility_of_element_located(Locators.SIDEBAR_ONGOING)).click()

        wait.until(EC.visibility_of_element_located(Locators.CREATE_SURVEY_BTN)).click()

        wait.until(EC.visibility_of_element_located(Locators.SURVEY_OPTION)).click()

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

    except Exception as e:
        try:
            iframe = driver.find_element("tag name", "iframe")
            driver.switch_to.frame(iframe)
            iframe_content = driver.page_source
            driver.switch_to.default_content()

            if "SERVER ERROR 500" in iframe_content or "Server Error" in iframe_content:
                msg = "Server Error 500 encountered."
                logging.error(msg)
                pytest.fail(msg)
        except Exception as iframe_error:
            logging.warning(f"Could not inspect iframe content: {iframe_error}")

        # Fallback if iframe logic fails or it's not a 500 error
        msg = f"Unexpected exception occurred: {str(e)}"
        logging.exception(msg)
        pytest.fail(msg)