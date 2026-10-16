import time
from utilities.screenshot import Screenshot
from utilities.logger import get_logger
import pytest
from pages.pim_page import HRM_PIMPage


logger = get_logger(__name__)

@pytest.mark.regression
def test_create_and_search_user(orange_hrm_login):
    pim_page = HRM_PIMPage(orange_hrm_login)
    logger.info("Creating a new user")
    emp_id = pim_page.create_user()
    Screenshot.capture(orange_hrm_login, f"PIM_Create_User_{emp_id}")

    logger.info("Searching for the newly created employee ID: %s", emp_id)
    pim_page.search_user(emp_id)
    Screenshot.capture(orange_hrm_login, f"PIM_User_Search_Result_{emp_id}")
    logger.info("Successfully created and found employee ID %s", emp_id)