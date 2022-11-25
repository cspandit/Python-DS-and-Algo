Feature: To test the working calculator

  @skip
  Scenario Outline: Add two numbers
    Given two inputs numbers are <num1> and <num2>
    When calculation is performed
    Then calculation should match expected result <result>

    Examples: Test Data
    | num1          | num2  |    | result |
    | 9             | 12    |    | 21     |
    | 5             | 15    |    | 20     |

  Scenario: Add wo number second test case
    Given two inputs numbers are 8 and 8
    When calculation is performed
    Then calculation should match expected result 16
