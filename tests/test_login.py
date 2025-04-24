import pytest
from pages.universal_locators import Locators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.order(2)
def test_login(driver, temp_email_store):
    locators = Locators(driver)

    wait = WebDriverWait(driver, 10)

    try:
        # Use email from store
        temp_email = temp_email_store.get("email")
        assert temp_email is not None, "Temp email not found in store"

        time.sleep(3)

        # Login process
        wait.until(EC.visibility_of_element_located(locators.LOGIN_EMAIL)).send_keys(temp_email)
        wait.until(EC.visibility_of_element_located(locators.LOGIN_PASSWORD)).send_keys(locators.SIGNUP_PASSWORD_VALUE)
        wait.until(EC.visibility_of_element_located(locators.LOGIN_BUTTON)).click()
        
        time.sleep(3)

        assert driver.current_url == "https://impak.app/dashboard"

    except TimeoutException as e:
        print(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure