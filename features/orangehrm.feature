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

  Scenario: Create an employee and find it using its generated ID
    Given I am logged in to OrangeHRM
    When I create an employee with generated details and retain its employee ID
    And I search using the returned employee ID
    Then the created employee is displayed in the search results
