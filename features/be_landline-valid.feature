
Feature: API generates data for user 
 Scenario Outline: Generate a new landline number
    Given I need landline number
     When Request <country> <amount>
    Then I receive <amount> of valid landline number for <country>

Examples:
  | country | amount |
  | Belgium | 100    |
  

