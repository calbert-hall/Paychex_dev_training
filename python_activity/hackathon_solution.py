from datetime import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
# from applitools.common import FileLogger
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from applitools.selenium import (
    logger,
    VisualGridRunner,
    ClassicRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)

import os
import os
import re

APPLIFASHIONV1 = "https://demo.applitools.com/gridHackathonV1.html"
APPLIFASHIONVDEV = "https://demo.applitools.com/tlcHackathonDev.html"
APPLIFASHIONV2 = "https://demo.applitools.com/gridHackathonV2.html"

username = "Applit465856618"
password = "Test1234"

#TODO set Dyanmic content
DYNAMIC_CONTENT = False

# ChromeDriver Headless Mode
HEADLESS = True

#TODO change the ENV_URL to change which environment is use
ENV_URL = "https://myappsimpn.paychex.com/"

#Useful selectors



def explicitWait(selector):
    waitSeconds = 10
    try:
        wait = WebDriverWait(web_driver, waitSeconds)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except:
        print("\nSelector '%s' did not load in '%s' seconds...\n" % (selector, waitSeconds))

def login(web_driver, eyes):
    try:
        # Navigate to the url we want to test
        # web_driver.get("https://myappsimpn.paychex.com/")
        # wait = WebDriverWait(web_driver, 10)
        web_driver.switch_to.frame("login")
        # explicitWait("div.col-sm-6:nth-child(3) > button:nth-child(1)")
        usernameField = web_driver.find_element_by_id("USER")
        usernameField.send_keys(username)
        web_driver.find_element_by_css_selector("div.col-sm-6:nth-child(3) > button:nth-child(1)").click()

        explicitWait("#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)")
        nextButton = web_driver.find_element_by_css_selector(
            "#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)")
        nextButton.click()

        secQuestion = web_driver.find_element_by_class_name("control-label").text
        answerSplit = re.split("[' '|?]", secQuestion)
        answer = answerSplit[len(answerSplit) - 2]
        web_driver.find_element_by_id("answer").send_keys(answer)
        web_driver.find_element_by_css_selector(
            "#appPlaceHolder > div.ng-scope > div > form > div:nth-child(2) > div > div > button:nth-child(2)").click()

        explicitWait(
            "#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)")
        web_driver.find_element_by_class_name("form-control").send_keys(password)
        web_driver.find_element_by_css_selector(
            "#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)").click()
        web_driver.switch_to_default_content()

        # this one fails
        explicitWait("#subapp-container > div.angular-subapp-wrapper.loaded > div > div > div > div > png-unified-header > div > div.flex-container > section.unified-header-information > unified-header-information > png-header-information > div > header > div.png-header-title-content > h4 > span")
        explicitWait("#app-dashboard-custom > div > div.custom-dash___grid.muuri > custom-dashboard-grid-item:nth-child(3) > div > custom-dashboard-grid-item-content > div > div > div > header > div > div")

        explicitWait('#main-content > fab-icon > message-indicator > png-badge > ng-transclude > ng-transclude > div')
        # Hide question mark button
        web_driver.execute_script("document.querySelector('#main-content > fab-icon > message-indicator > png-badge > ng-transclude > ng-transclude > div').style.visibility = 'hidden';")
        print("Login Complete")
    except Exception as e:
        # eyes.abort_async()
        print("Exception in Login: " + str(e))


def set_up(eyes):

    # You can get your api key from the Applitools dashboard
    eyes.configure.set_api_key(os.environ["APPLITOOLS_API_KEY"])

    # create a new batch info instance and set it to the configuration
    eyes.configure.set_batch(BatchInfo("Hackathon Batch - Python"))
    eyes.configure.set_layout_breakpoints(True)

    # eyes.configure.set_server_url("https://paychexeyes.applitools.com/") //TODO-CAH uncomment this for Paychex
    # Add browsers with different viewports
    # Add mobile emulation devices in Portrait mode
    (
        eyes.configure.add_browser(1000, 800, BrowserType.CHROME),
        eyes.configure.add_browser(1024, 768, BrowserType.FIREFOX),
        eyes.configure.add_device_emulation(DeviceName.iPhone_X),
        eyes.configure.add_device_emulation(DeviceName.iPad_Pro)
    )


def ultra_fast_test(web_driver, eyes):
    try:
        # Navigate to the url we want to test
        web_driver.get(ENV_URL)

        # Call Open on eyes to initialize a test session
        eyes.open(
            web_driver, "Paychex", "SOLUTION: Paychex Flex", {"width": 1200, "height": 800}
        )

        # check the login page with fluent api, see more info here
        # https://applitools.com/docs/topics/sdk/the-eyes-sdk-check-fluent-api.html
        print("Login workflow...")
        login(web_driver, eyes)
        print("Sleeping....")
        time.sleep(7)
        print("Checking Main page....")
        #eyes.check("Main Page", Target.window()) #TODO fully might need

        eyes.check("Dashboard Region",
                   Target.region("#appContainer").fully().scroll_root_element("#appContainer"))

        selectMenuButton(web_driver, eyes)
        goToCompanyDetails(web_driver)
        time.sleep(4)
        #eyes.check("Company Details", Target.window()) #TODO fully might need
        eyes.check("Company Details",
                    Target.region("#appContainer").fully().scroll_root_element("#appContainer"))

        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)

def selectMenuButton(web_driver, eyes):
    try:
        button = web_driver.find_element_by_css_selector(
            "#appContainer > div.top-bar > div.left-nav-trigger-container.visible")
        button.click()
    except NoSuchElementException as e:
        print(e)
        print("Menu button not found.")

def goToCompanyDetails(web_driver):
    try:
        link = web_driver.find_element_by_css_selector(
            "#appContainer > md-sidenav > div.left-nav-content-container > div > div > div.list-wrapper-wrapper > div:nth-child(1) > div:nth-child(6) > div > div > a > span"
        )
        link.click()
        explicitWait("#paychex\.app\.company\.profile > div > div.png-error-transclude.full-height > div > div > div.right-column > png-card > div > header > div.png-card-trigger-wrapper")
    except Exception as e:
        print(e)


def tear_down(web_driver, runner):
    # Close the browser
    web_driver.quit()

    # we pass false to this method to suppress the exception that is thrown if we
    # find visual differences
    all_test_results = runner.get_all_test_results()
    print(all_test_results)

chrome_options = Options()
chrome_options.headless = HEADLESS
# web_driver = webdriver.Chrome(options=chrome_options)
# Create a new chrome web driver

web_driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
#Chrome(ChromeDriverManager(version="99.0.4844.51").install(), options=chrome_options)

# This is just a setting that sets the time for waiting for elements to be 10s
web_driver.implicitly_wait(10)
# Create a runner with concurrency of 1
runner = VisualGridRunner(5)

# Create Eyes object with the runner, meaning it'll be a Visual Grid eyes.
eyes = Eyes(runner)

set_up(eyes)
# logger.set_logger(FileLogger("./logs/applitools_" + str(datetime.now()) + ".log"))

try:
    # ⭐️ Note to see visual bugs, run the test using the above URL for the 1st run.
    # but then change the above URL to https://demo.applitools.com/index_v2.html
    # (for the 2nd run)
    ultra_fast_test(web_driver, eyes)
finally:
    tear_down(web_driver, runner)
