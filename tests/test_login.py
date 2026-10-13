import pytest
from pages.login_page import HRM_LoginPage
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)
LOGIN_USERS = ConfigReader.get_config("users")


@pytest.mark.smoke
def test_hrm_login(orange_hrm_login):
    logger.info("Waiting for the HRM home page")
    #time.sleep(10)
    assert orange_hrm_login.title == "OrangeHRM", f"Expected title 'OrangeHRM' but got '{orange_hrm_login.title}'"
    logger.info("Capturing HRM home page screenshot")
    Screenshot.capture(orange_hrm_login, "HRM_Home_Page")
    logger.info("Successfully navigated to HRM home page")

@pytest.mark.regression
@pytest.mark.parametrize(
    "user",
    LOGIN_USERS.values(),
    ids=LOGIN_USERS.keys(),
)
def test_hrm_multi_login(driver, user):
    logger.info("Waiting for the HRM home page")
    HRM_LoginPage(driver).hrm_login_page(
        driver,
        user["username"],
        user["password"],
    )
    assert driver.title == "OrangeHRM", (
        f"Expected title 'OrangeHRM' but got '{driver.title}' "
        f"for user '{user['username']}'"
    )
    logger.info(f"Capturing HRM home page screenshot for user '{user['username']}'")
    Screenshot.capture(driver,  f"HRM_Home_Page_user_{user['username']}")
    logger.info("Successfully navigated to HRM home page")