import time
from utilities.screenshot import Screenshot
from utilities.logger import get_logger
import pytest
from pages.pim_page import HRM_PIMPage


logger = get_logger(__name__)

@pytest.mark.smoke
def test_search_user(orange_hrm_login,):
    logger.info("Searching for user")
    HRM_PIMPage(orange_hrm_login).search_user()
    Screenshot.capture(orange_hrm_login, "PIM_User_Search_Result")
    logger.info("Successfully searched for user and captured screenshot of search result")

@pytest.mark.regression
def test_create_user(orange_hrm_login):
    logger.info("Creating a new user")
    HRM_PIMPage(orange_hrm_login).create_user()
    Screenshot.capture(orange_hrm_login, "PIM_Create_User")
    logger.info("Successfully created a new user and captured screenshot of the process")