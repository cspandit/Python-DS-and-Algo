*** Settings ***

Library    JSONLibrary
Library    OperatingSystem
Library    Collections

*** Test Cases ***
TestCase 1
    ${json_object}=    Load Json From File    /Users/shekharpandit/PycharmProjects/Python-DS-and-Algo_new/Testing Framework/Robot/TestCases/TestData/test.json
    ${phone}    Get Value From Json    ${json_object}    $.Address.PhoneNumber[0]
    Log To Console    ${phone}
    Should Be Equal    ${phone[0]}    9663822448

