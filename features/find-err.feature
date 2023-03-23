
Feature: API is alright
 Scenario Outline: Generate data
    Given I send a GET request to API 
     When I request data for <link_name> <response_name>
    Then I receive adequate response

Examples:
  | link_name | response_name |
  # | bis       | bis           |
  # | insz      | inszs         |
  # | kbo       | kbos          |
  # | nihii     | nihii         |
  # | plates    | plates        |
  # | polis     | polisnummer   |
  # | riziv     | riziv         |
  # | telephone | phoneNumber   |
  # | uuid      | uuids         |
  # | lorem      | lorem        |
  

