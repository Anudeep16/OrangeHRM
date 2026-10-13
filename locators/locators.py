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
        "xpath": "//span[normalize-space()='PIM']"
    }
    emp_id={
        "xpath":"//div//label[contains(text(),'Employee Id')]//following::input[1]"
    }
    search_btn={
        "xpath":"//div//button[@type='submit']"
    }
    form_loader={
        "css_selector":".oxd-form-loader"
    }
    search_result={
        "xpath":
            #"(//div[@role='rowgroup'])[2]//div[2]"
            "//div[@role='table']//div[contains(text(),'0304')]//following::div[2][contains(text(),'Rahul')]"
    }
    add_emp_btn={
        "xpath":"//a[normalize-space()='Add Employee']"
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
    save_btn={
        "xpath":"//button[@type='submit' and normalize-space()='Save']"
    }
    dashboard={
        "xpath": "//h6[normalize-space()='Dashboard']"
    }
