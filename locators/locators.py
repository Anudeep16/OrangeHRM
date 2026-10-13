# Grouping selectors behind named attributes separates page-object actions from UI locator details.
class LoginLocators:
    username = {
        "name": "username"
    }

    password = {
        "name": "password"
    }

    login_btn = {
        "xpath": "//button[@type='submit']"
    }


class HomePageLocators:
    pim = {
        "xpath": "(//span[contains(text(),'')])[2]"
    }
    emp_id={
        "xpath":"//div//label[contains(text(),'Employee Id')]//following::input[1]"
    }
    search_btn={
        "xpath":"//div//button[@type='submit']"
    }
    search_result={
        "xpath":
            #"(//div[@role='rowgroup'])[2]//div[2]"
            "//div[@role='table']//div[contains(text(),'0304')]//following::div[2][contains(text(),'Rahul')]"
    }
    add_emp_btn={
        "xpath":"//li//a[contains(text(),'Add Employee')]"
    }
    first_name={
        "xpath":"//div//input[@name='firstName']"
    }
    middle_name={
        "xpath":"//div//input[@name='middleName']"
    }
    last_name={
        "xpath":"//div//input[@name='lastName']"
    }

