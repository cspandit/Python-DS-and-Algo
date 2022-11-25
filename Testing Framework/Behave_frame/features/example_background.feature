Feature: This is to test background feature

  # This is like setup. Background steps are executed before every scenarios
  # behave -f allure_behave.formatter:AllureFormatter -0 reports/ features/ - to generate allure json report
  #  allure serve <path_to_allure_json_report> - to generate html report
  # Using tag: behave <fetaure_file> --tags=<tag_name> : execute scenarios with given tag
  # Using tag: behave <fetaure_file> --tags=~<tag_name> : skip scenarios with given tag
  # hooks : environment.py in steps folder
#  before_feature(context, feature) − Executes prior every feature.
#
#  before_scenario(context, scenario) − Executes prior every scenario.
#
#  before_step(context, step) − Executes prior every step.
#
#  before_tag(context, tag) − Executes prior every tag.
#
#  before_all(context) − Executes prior everything.
#
#  after_feature(context, feature) − Executes post every feature.
#
#  after_scenario(context, scenario) − Executes post every scenario.
#
#  after_step(context, step) − Executes post every step.
#
#  after_tag(context, tag) − Executes post every tag.
#
#  after_all(context) − Executes post everything.

  Background: To Enter Inputs
    Given : Two inputs are 12 and 2
    When : Calculation is done

  @Test
  Scenario: Addition of two numbers
    Then : Calculated value is 14


  Scenario: Subtraction of two numbers
    Then : Calculated value is 10

  Scenario: Multiplication of two numbers
    Then : Calculated value is 10

