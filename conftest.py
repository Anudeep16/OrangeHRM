from utilities.config_reader import ConfigReader
import pytest
from selenium import webdriver
from pages.login_page import HRM_LoginPage
from utilities.logger import get_logger


logger = get_logger(__name__)


@pytest.fixture(scope="function")
def driver(request):

    logger.info("Starting Chrome WebDriver")
    options = webdriver.ChromeOptions()

    if request.config.getoption("--headless"):
        options.add_argument("--headless")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--force-device-scale-factor=1")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    logger.info("Chrome WebDriver started and maximized")
    # Common implicit wait for all tests using this driver
    driver.implicitly_wait(10)

    yield driver

    logger.info("Closing Chrome WebDriver")
    driver.quit()
    logger.info("Chrome WebDriver closed")


def pytest_sessionstart(session):
    logger.info("Pytest session started")


def pytest_sessionfinish(session, exitstatus):
    logger.info("Pytest session finished with exit status %s", exitstatus)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        logger.error(
            "Test %s failed during %s: %s",
            item.nodeid,
            report.when,
            report.longrepr,
        )
    elif report.when == "call":
        logger.info("Test %s passed", item.nodeid)


def pytest_addoption(parser):

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome in headless mode",
    )
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment Name",
    )


@pytest.fixture(scope="function")
def orange_hrm_login(driver, request):

    env = request.config.getoption("--env")
    logger.info("Loading configuration for environment '%s'", env)
    config = ConfigReader.get_config(env)
    logger.info("Opening application URL: %s", config["url"])
    driver.get(config["url"])
    login_page = HRM_LoginPage(driver)

    logger.info("Starting login flow")
    login_page.hrm_login_page(
        driver,
        config["username"],
        config["password"],
    )
    logger.info("Login flow completed")
    yield driver