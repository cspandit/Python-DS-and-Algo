*** Settings ***
Library  RequestsLibrary
Library    Collections


*** Variables ***
${base_url}    https://reqres.in/api/users

*** Test Cases ***
Test_Case_One_Get_Users
    ${headers}=         Create Dictionary    
    ...                 x-api-key=reqres_d5ca6d1bc208462fa9ba94c2e5e585b7
    ...                 Content-Type=application/json

    create Session      my_session    ${base_url}    headers=${headers}
    ${response}=        GET On Session    my_session    /
    Log To Console      ${response.status_code}
    #Log To Console     ${response.text}
    ${status_code}=     Convert To String    ${response.status_code}
    Should Be Equal     ${status_code}    200
    ${response_body}=   Set Variable    ${response.content}
    Should Contain      ${response_body}    tracey.ramos@reqres.in
    #Log To Console     ${response.headers}
    ${content_type}     Get From Dictionary    ${response.headers}    Content-Type
    Should Be Equal     ${content_type}    application/json; charset=utf-8
    
Test_Case_Two_Create_user
    ${body}=    Create Dictionary    name=Chandra    job=engineer
    ${headers}    Create Dictionary    x-api-key=reqres_d5ca6d1bc208462fa9ba94c2e5e585b7

    Create Session    post_session    ${base_url}    
    ${responses}=    POST On Session    post_session    /    data=${body}    headers=${headers}
    ${status_code}=    Convert To String    ${responses.status_code}
    Log To Console    ${responses.content}
    Should Be Equal    ${status_code}    201
    