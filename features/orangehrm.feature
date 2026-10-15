Feature: OrangeHRM login and employee management
  As an HR administrator
  I want to log in and manage employee records
  So that I can verify the main OrangeHRM workflows

  Scenario: Log in with the selected environment account
    Given the OrangeHRM login page is open
    When I log in with the account configured for the selected environment
    Then the OrangeHRM dashboard is displayed

  Scenario Outline: Log in with each configured user account
    Given the OrangeHRM login page is open
    When I log in with the configured "<account>" account
    Then the OrangeHRM dashboard is displayed

    Examples:
      | account |
      | admin   |
      | user1   |
      | user2   |

  Scenario: Find an existing employee by employee ID
    Given I am logged in to OrangeHRM
    When I search for employee ID "0304" in PIM
    Then the matching employee is displayed in the search results

  Scenario: Create a new employee
    Given I am logged in to OrangeHRM
    When I open PIM and choose Add Employee
    And I enter generated employee details and save the form
    Then the new employee record is saved
