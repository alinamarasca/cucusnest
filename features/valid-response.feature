
Feature: API generates valid response 

Scenario Outline: API's response corresponds with input
    Given I request 
     When I send request <isGenderKnown> <isDateOfBirthKnown> <amount> <date>
     Then response is valid for the <date> and <isGenderKnown>
     

Examples:
  | isGenderKnown | isDateOfBirthKnown | amount | date       | 
  | true          | true               | 1      | ''         | 
  | true          | true               | 1      | 1967-11-10 | 
  | false         | false              | 1      | ''         | 
  | false         | true               | 1      | 2023-03-19 |
  

