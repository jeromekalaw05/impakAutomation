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

@pytest.mark.order(5)  # Adjust the order as needed
def test_add_group(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # --- Step 1: Navigate to "Community" and "Groups" ---
        community_sidebar_link = wait.until(
            EC.element_to_be_clickable(Locators.SIDEBAR_COMMUNITY)
        )
        community_sidebar_link.click()
        print("Clicked on 'Community'.")
        time.sleep(1)  # Small wait for the menu to open

        groups_link = wait.until(
            EC.element_to_be_clickable(Locators.GROUPS_LINK)
        )
        groups_link.click()
        print("Clicked on 'Groups'.")
        time.sleep(2)

        # --- Step 2: Click the "+ Create" Button ---
        create_button = wait.until(
            EC.element_to_be_clickable(Locators.CREATE_GROUP_BUTTON)
        )
        create_button.click()
        print("Clicked on 'Create'.")
        time.sleep(2)

        # --- Step 3: Fill in the "Group Name" Field ---
        group_name_input = wait.until(
            EC.presence_of_element_located(Locators.GROUP_NAME_INPUT_FIELD)
        )
        group_name_input.send_keys("Add Group Test")
        print("Entered 'Add Group Test' as the group name.")
        time.sleep(1)

        # --- Step 4: Select "Jake Smith" from the "Group Leader" Dropdown ---
        group_leader_dropdown = Select(wait.until(
            EC.presence_of_element_located(Locators.GROUP_LEADER_DROPDOWN)
        ))
        group_leader_dropdown.select_by_visible_text("Jake Smith")
        print("Selected 'Jake Smith' as the group leader.")
        time.sleep(1)

        # --- Step 5: Click the "Add New" Button ---
        add_new_button = wait.until(
            EC.element_to_be_clickable(Locators.ADD_NEW_GROUP_BUTTON)
        )
        add_new_button.click()
        print("Clicked 'Add New'.")
        time.sleep(3)

        print("Group creation process automated successfully!")

    except TimeoutException as e:
        logging.exception(f"TimeoutException: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure

    except Exception as e:
        logging.exception(f"Exception occurred: {str(e)}")
        raise  # Re-raise the exception to stop the test in case of failure