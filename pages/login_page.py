import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import LoginLocators, HomePageLocators
from utilities.screenshot import Screenshot
from utilities.logger import get_logger

logger = get_logger(__name__)


# Abstraction: tests use this login operation instead of handling Selenium elements directly.
class HRM_LoginPage:

    def __init__(self, driver):
        # Keep the page's browser and locator dependencies together.
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.login_locators = LoginLocators()
        self.homepage_locators = HomePageLocators()


    def hrm_login_page(self, driver, username, password):
        logger.info("Opening OrangeHRM login page")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        logger.info("Waiting for login page to load")
        logger.info("Capturing login page screenshot")
        Screenshot.capture(self.driver, "HRM_Login_Page")
        logger.info("Entering username")
        self.driver.find_element(By.NAME, self.login_locators.username["name"]).send_keys(username)
        logger.info("Entering password")
        self.driver.find_element(By.NAME, self.login_locators.password["name"]).send_keys(password)
        logger.info("Submitting login form")
        self.driver.find_element(By.XPATH, self.login_locators.login_btn["xpath"]).click()
        logger.info("Waiting for login to complete")
