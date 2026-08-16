*** Settings ***
Library    Calculator.py
Library    OperatingSystem


*** Variables ***

*** Test Cases ***
Test Platform Cases
    Run Platform Specific Test
Test With Data Set
    [Template]    Test Multiply
    2    3    6
    4    2    8
    10    12    120
    


*** Keywords ***
Run Platform Specific Test
    ${platform}=    Evaluate    sys.platform    sys
    Log To Console     ${platform}
    Run Keyword If    '${platform}' == 'darwin'    Test Divide
    Run Keyword If    '${platform}' == 'win'        Test Add

Test Multiply
    [Arguments]    ${a}    ${b}    ${e_result}
    ${result}=    multiply    ${a}    ${b}
    Should Be Equal As Integers    ${result}     ${result}
    
Test Divide
    ${result}=    divide    10    5
    Should Be Equal As Integers    ${result}    2

Test Add
    ${result}=    add    10    5
    Should Be Equal As Integers    ${result}    15
    
