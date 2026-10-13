import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import LoginLocators, HomePageLocators
from utilities.screenshot import Screenshot
from utilities.logger import get_logger
import random
from selenium.webdriver.common.keys import Keys


# 1. Generate a random name from a pre-defined list
names_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan","Shyam","Rahul","Kumar","Sharma","Ramesh","Suresh","Anita","Priya","Vikram","Amit","Singa","Roy","Kiran","Ravi","Nisha","Pooja"]
random_f_name = random.choice(names_list)
random_m_name = random.choice(names_list)
random_l_name = random.choice(names_list)

# 2. Generate a random integer between 1000 and 9999 (inclusive)
random_number = random.randint(1000, 9999)


logger = get_logger(__name__)


# Abstraction: tests call PIM operations without managing Selenium elements and waits themselves.
class HRM_PIMPage:

    def __init__(self, driver):
        # Encapsulate the browser and this page's locator dependencies.
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.login_locators = LoginLocators()
        self.homepage_locators = HomePageLocators()

    def search_user(self):
        logger.info("Searching for user")
        pim_ele = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.homepage_locators.pim["xpath"])))
        pim_ele.click()
        self.driver.find_element(By.XPATH, self.homepage_locators.emp_id["xpath"]).send_keys("0304")
        self.driver.find_element(By.XPATH, self.homepage_locators.search_btn["xpath"]).click()
        assert self.driver.find_element(By.XPATH, self.homepage_locators.search_result["xpath"]).is_displayed(), "Search result not found"
        logger.info("User search completed")

    def create_user(self):
        logger.info("Creating a new user")
        pim_ele = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.homepage_locators.pim["xpath"])))
        pim_ele.click()
        add_employee = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.add_emp_btn["xpath"])
            )
        )
        add_employee.click()
        self.driver.find_element(By.XPATH, self.homepage_locators.first_name["xpath"]).send_keys({random_f_name})
        self.driver.find_element(By.XPATH, self.homepage_locators.middle_name["xpath"]).send_keys({random_m_name})
        self.driver.find_element(By.XPATH, self.homepage_locators.last_name["xpath"]).send_keys({random_l_name})
        #self.driver.find_element(By.XPATH, self.homepage_locators.emp_id["xpath"]).clear()
        self.driver.find_element(By.XPATH, self.homepage_locators.emp_id["xpath"]).send_keys(Keys.CONTROL, "a")
        self.driver.find_element(By.XPATH, self.homepage_locators.emp_id["xpath"]).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, self.homepage_locators.emp_id["xpath"]).send_keys(str(random_number))
        self.driver.find_element(By.XPATH, self.homepage_locators.search_btn["xpath"]).click()
        # Add more steps to fill in the user details and submit the form
        logger.info("New user created successfully")
