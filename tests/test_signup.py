import time
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.order(1)
def test_signup(driver, temp_email_store):
    locators = Locators(driver)

    driver.get(locators.IMPAK_URL)

    wait = WebDriverWait(driver, 10)

    try:
        # Signup process
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_LINK_BUTTON)).click()

        # Save the main tab handle
        main_tab = driver.current_window_handle

        time.sleep(5)

        # Open new tab and switch to it
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        # Go to temp-mail and get email
        driver.get(locators.TEMP_MAIL_URL)
        time.sleep(10)
        email_field = wait.until(EC.presence_of_element_located(locators.TEMP_MAIL_EMAIL))
        temp_email = email_field.get_attribute("value")

        temp_email_store["email"] = temp_email

        # Switch back to main signup tab
        driver.switch_to.window(main_tab)

        wait.until(EC.visibility_of_element_located(locators.SIGNUP_FIRST_NAME_INPUT)).send_keys(locators.SIGNUP_FIRST_NAME_VALUE)
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_LAST_NAME_INPUT)).send_keys(locators.SIGNUP_LAST_NAME_VALUE)
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_EMAIL_INPUT)).send_keys(temp_email)
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_PASSWORD_INPUT)).send_keys(locators.SIGNUP_PASSWORD_VALUE)
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_CONFIRM_PASSWORD_INPUT)).send_keys(locators.SIGNUP_PASSWORD_VALUE)
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_TERMS_CHECKBOX)).click()
        wait.until(EC.visibility_of_element_located(locators.SIGNUP_BUTTON)).click()

        time.sleep(3)
        
        assert driver.current_url == "https://impak.app/dashboard"

        wait.until(EC.visibility_of_element_located(locators.LOGOUT_LINK_BUTTON)).click()

    except TimeoutException as e:
        print(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure