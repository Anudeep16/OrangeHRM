import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        self.wait = WebDriverWait(driver, 30)
        self.login_locators = LoginLocators()
        self.homepage_locators = HomePageLocators()


    def hrm_login_page(self, driver, username, password):
        logger.info("Opening OrangeHRM login page")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        logger.info("Waiting for login page to load")
        logger.info("Capturing login page screenshot")
        Screenshot.capture(self.driver, "HRM_Login_Page")
        logger.info("Entering username")
        username_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, self.login_locators.username["name"])
            )
        )
        username_field.send_keys(username)
        logger.info("Entering password")
        password_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, self.login_locators.password["name"])
            )
        )
        password_field.send_keys(password)
        logger.info("Submitting login form")
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.login_locators.login_btn["xpath"])
            )
        )
        login_button.click()
        logger.info("Waiting for login to complete")
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.homepage_locators.dashboard["xpath"])
            )
        )
