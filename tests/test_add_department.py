import logging
import time
import pytest
from pages.universal_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.order(6)  # Adjust the order as needed
def test_add_department(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # --- Step 1: Navigate to "Community" and "Departments" ---
        community_sidebar_link = wait.until(
            EC.element_to_be_clickable(Locators.SIDEBAR_COMMUNITY)
        )
        community_sidebar_link.click()
        print("Clicked on 'Community'.")
        time.sleep(1)  # Small wait for the menu to open

        departments_link = wait.until(
            EC.element_to_be_clickable(Locators.DEPARTMENTS_LINK)
        )
        departments_link.click()
        print("Clicked on 'Departments'.")
        time.sleep(2)

        # --- Step 2: Click the "+ Create" Button ---
        create_button = wait.until(
            EC.element_to_be_clickable(Locators.CREATE_BUTTON)
        )
        create_button.click()
        print("Clicked on 'Create'.")
        time.sleep(2)

        # --- Step 3: Fill in the "Department Name" Field ---
        department_name_input = wait.until(
            EC.presence_of_element_located(Locators.DEPARTMENT_NAME_INPUT_FIELD)
        )
        department_name_input.send_keys("Testing Department")
        print("Entered 'Testing Department' as the department name.")
        time.sleep(1)

        # --- Step 4: Select "Jake Smith" as the "Department Head" ---
        department_head_dropdown = Select(wait.until(
            EC.presence_of_element_located(Locators.DEPARTMENT_HEAD_DROPDOWN)
        ))
        department_head_dropdown.select_by_visible_text("Jake Smith")
        print("Selected 'Jake Smith' as the department head.")
        time.sleep(1)

        # --- Step 5: Click the "Add New" Button ---
        add_new_department_button = wait.until(
            EC.element_to_be_clickable(Locators.ADD_NEW_DEPARTMENT_BUTTON)
        )
        add_new_department_button.click()
        print("Clicked 'Add New'.")
        time.sleep(3)

        print("Department creation process automated successfully!")

    except TimeoutException as e:
        logging.exception(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure