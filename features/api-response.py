
Feature: API generates data for user 
 Scenario Outline: Generate a new BIS
    Given I request BIS
     When I send a GET request <isGenderKnown> <isDateOfBirthKnown> <amount> <date>
    Then the response status code should be 200

Examples:
  | isGenderKnown | isDateOfBirthKnown | amount | date       |
  | true          | true               | 1      | 1967-11-10 |
  | true          | false              | 1      | ''         |
  | false         | false              | 1      | ''         |
  | false         | true               | 1      | 2020-04-07 |
  

