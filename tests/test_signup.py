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
        signup_link = wait.until(EC.element_to_be_clickable(locators.SIGNUP_LINK_BUTTON))
        assert signup_link.is_displayed(), "Sign up link is not visible."
        signup_link.click()

        # Save the main tab handle
        main_tab = driver.current_window_handle

        time.sleep(5)

        # Open new tab and switch to it
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        # Go to temp-mail and get email
        driver.get(locators.TEMP_MAIL_URL)
        time.sleep(10)
        temp_email_field = wait.until(EC.presence_of_element_located(locators.TEMP_MAIL_EMAIL))
        temp_email = temp_email_field.get_attribute("value")

        temp_email_store["email"] = temp_email

        # Switch back to main signup tab
        driver.switch_to.window(main_tab)

        firstname_field = wait.until(EC.visibility_of_element_located(locators.SIGNUP_FIRST_NAME_INPUT))
        assert firstname_field.is_displayed(), "First name field in signup not displayed"
        firstname_field.send_keys(locators.SIGNUP_FIRST_NAME_VALUE)

        lastname_field = wait.until(EC.visibility_of_element_located(locators.SIGNUP_LAST_NAME_INPUT))
        assert lastname_field.is_displayed(), "Last name field in signup is not displayed"
        lastname_field.send_keys(locators.SIGNUP_LAST_NAME_VALUE)

        email_field = wait.until(EC.visibility_of_element_located(locators.SIGNUP_EMAIL_INPUT))
        assert email_field.is_displayed(), "Email field in signup is not displayed"
        email_field.send_keys(temp_email)

        # Check if correct email is copied from temp-mail
        email_value = email_field.get_attribute("value")
        assert temp_email == email_value, "Email do not match"

        password_field = wait.until(EC.visibility_of_element_located(locators.SIGNUP_PASSWORD_INPUT))
        assert password_field.is_displayed(), "Password field in signup is not displayed"
        password_field.send_keys(locators.SIGNUP_PASSWORD_VALUE)

        confirmpass_field = wait.until(EC.visibility_of_element_located(locators.SIGNUP_CONFIRM_PASSWORD_INPUT))
        assert confirmpass_field.is_displayed(), "Confirm pass field in signup is not displayed"
        confirmpass_field.send_keys(locators.SIGNUP_PASSWORD_VALUE)

        # Check if password and confirm password are equal
        password_value = password_field.get_attribute("value")
        confirmpass_value = confirmpass_field.get_attribute("value")
        assert password_value == confirmpass_value, "Password and Confirm Password do not match."

        checkbox = wait.until(EC.element_to_be_clickable(locators.SIGNUP_TERMS_CHECKBOX))
        assert checkbox.is_displayed(), "Checkbox is not displayed"
        checkbox.click()

        signup_button = wait.until(EC.element_to_be_clickable(locators.SIGNUP_BUTTON))
        assert signup_button.is_displayed(), "Signup button is not displayed"
        signup_button.click()

        time.sleep(3)
        
        assert driver.current_url == "https://impak.app/dashboard"
        
        time.sleep(2)

        logout_button = wait.until(EC.element_to_be_clickable(locators.LOGOUT_LINK_BUTTON))
        assert logout_button.is_displayed(), "Logout button is not visible"
        logout_button.click()

    except TimeoutException as e:
        print(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure