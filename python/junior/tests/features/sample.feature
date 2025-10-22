Feature: Sample task API test
  Scenario: Get all tasks
    Given the API is running
    When I send a GET request to "/tasks"
    Then I receive a 200 status code