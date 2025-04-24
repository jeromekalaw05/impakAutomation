import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def temp_email_store():
    return {}  # Dictionary to store shared values