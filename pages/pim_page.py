import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import HomePageLocators
from utilities.logger import get_logger


NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Shyam", "Rahul",
    "Kumar", "Sharma", "Ramesh", "Suresh", "Anita", "Priya", "Vikram",
    "Amit", "Singa", "Roy", "Kiran", "Ravi", "Nisha", "Pooja",
]


logger = get_logger(__name__)


# Abstraction: tests call PIM operations without managing Selenium elements and waits themselves.
class HRM_PIMPage:

    def __init__(self, driver):
        # Encapsulate the browser and this page's locator dependencies.
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.homepage_locators = HomePageLocators()

    def create_user(self) -> str:
        logger.info("Creating a new user")
        pim_ele = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.homepage_locators.pim["xpath"])))
        pim_ele.click()
        add_employee = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.add_emp_btn["xpath"])
            )
        )
        add_employee.click()
        for locator, value in (
            (self.homepage_locators.first_name, random.choice(NAMES)),
            (self.homepage_locators.middle_name, random.choice(NAMES)),
            (self.homepage_locators.last_name, random.choice(NAMES)),
        ):
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator["xpath"]))
            ).send_keys(value)

        emp_id = str(random.randint(1000, 9999))
        employee_id_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.homepage_locators.emp_id["xpath"])
            )
        )
        employee_id_field.send_keys(Keys.CONTROL, "a")
        employee_id_field.send_keys(Keys.DELETE)
        employee_id_field.send_keys(emp_id)
        entered_emp_id = employee_id_field.get_attribute("value")
        if not entered_emp_id:
            raise AssertionError("Employee ID was not entered in the Add Employee form")
        self.wait.until(
            EC.invisibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    self.homepage_locators.form_loader["css_selector"],
                )
            )
        )
        save_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.save_btn["xpath"])
            )
        )
        save_button.click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.homepage_locators.personal_details["xpath"])
            )
        )
        logger.info("New user created with Employee ID: %s", entered_emp_id)
        return entered_emp_id

    def search_user(self, emp_id: str) -> None:
        if not emp_id:
            raise ValueError("Employee ID must not be empty")

        logger.info("Searching for employee ID: %s", emp_id)
        pim_ele = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.pim["xpath"])
            )
        )
        pim_ele.click()
        employee_list = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.emp_list_btn["xpath"])
            )
        )
        employee_list.click()

        employee_id_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.homepage_locators.emp_id["xpath"])
            )
        )
        employee_id_field.send_keys(Keys.CONTROL, "a")
        employee_id_field.send_keys(Keys.DELETE)
        employee_id_field.send_keys(emp_id)

        self.wait.until(
            EC.invisibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    self.homepage_locators.form_loader["css_selector"],
                )
            )
        )
        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homepage_locators.search_btn["xpath"])
            )
        )
        search_button.click()

        result_locator = (
            By.XPATH,
            self.homepage_locators.search_result["xpath"].format(emp_id),
        )
        self.wait.until(EC.visibility_of_element_located(result_locator))
        logger.info("Found employee with ID: %s", emp_id)
