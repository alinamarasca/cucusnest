
Feature: API generates data for user 

  Scenario: Generate a new BIS
    Given I request BIS
     When I send a GET request
      | isGenderKnown | isDateOfBirthKnown | amount |
      | False         | False              | 1      |
    Then the response status code should be 200

