*** Settings ***
Library     SeleniumLibrary
Library     EyesLibrary     web_ufg
Library     PaychexLibrary

Test Setup    Setup
Test Teardown    Teardown

*** Variables ***
&{LOGO}     id=hplogo                 xpath=//*[@id="hplogo"]
${BROWSER}        Chrome
${URL}      https://myappsimpn.paychex.com/
&{APPCONTAINER}     id=appContainer

*** Keywords ***
Setup
    Open Browser                              ${URL}      ${BROWSER}

Teardown
    Close All Browsers
    Eyes Abort Async


*** Test Cases ***

Check Dashboard and Company Details
    login
    Eyes Open
    ${element}=     Get WebElement          id:appContainer
    wait until element is visible   id:appContainer
    # TODO Create eyes check here
    selectMenuButton
    goToCompanyDetails
    wait until element is visible   id:appContainer
    # TODO create eyes check here
    Eyes Close Async


