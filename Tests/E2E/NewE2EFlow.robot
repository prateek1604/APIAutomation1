*** Settings ***
Documentation    This is for the E2E Flow of UI and API
Resource        ../../Resources/UIPages/Navigation.robot
Library         ../../Resources/API/Reqres_API.py

*** Variables ***
${dict}         test

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Given I navigate to reqres.in
    When I get endpoint from UI
    Then I hit endpoint to test the API
