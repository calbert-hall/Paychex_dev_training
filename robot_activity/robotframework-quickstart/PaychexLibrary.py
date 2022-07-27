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
from robot.libraries.BuiltIn import BuiltIn
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
import re
import pytest

username = "Applit465856618"
password = "Test1234"

# ChromeDriver Headless Mode
HEADLESS = True
ENV_URL = "https://myappsimpn.paychex.com/"

class PaychexLibrary:

    def get_browser_driver(self):
        return BuiltIn().get_library_instance('SeleniumLibrary').driver

    def explicitWait(self, selector, web_driver):
        waitSeconds = 10
        try:
            wait = WebDriverWait(web_driver, waitSeconds)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except:
            print("\nSelector '%s' did not load in '%s' seconds...\n" % (selector, waitSeconds))


    def login(self):
        try:
            print("Logging in...")
            web_driver = self.get_browser_driver()
            web_driver.implicitly_wait(10)
            web_driver.switch_to.frame("login")
            usernameField = web_driver.find_element_by_id("USER")
            usernameField.send_keys(username)
            web_driver.find_element_by_css_selector("div.col-sm-6:nth-child(3) > button:nth-child(1)").click()

            self.explicitWait("#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)", web_driver)
            print("Finding continue button...")
            # I want to answer a security question -> continue
            nextButton = web_driver.find_element_by_css_selector(
                "#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)")
            nextButton.click()

            secQuestion = web_driver.find_element_by_class_name("control-label").text
            answerSplit = re.split("[' '|?]", secQuestion)
            answer = answerSplit[len(answerSplit) - 2]
            web_driver.find_element_by_id("answer").send_keys(answer)
            web_driver.find_element_by_css_selector(
                "#appPlaceHolder > div.ng-scope > div > form > div:nth-child(2) > div > div > button:nth-child(2)").click()

            self.explicitWait(
                "#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)",
                web_driver)
            web_driver.find_element_by_class_name("form-control").send_keys(password)
            web_driver.find_element_by_css_selector(
                "#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)").click()
            web_driver.switch_to_default_content()

            self.explicitWait(
                "#subapp-container > div.angular-subapp-wrapper.loaded > div > div > div > div > png-unified-header > div > div.flex-container > section.unified-header-information > unified-header-information > png-header-information > div > header > div.png-header-title-content > h4 > span",
                web_driver)
            self.explicitWait(
                "#app-dashboard-custom > div > div.custom-dash___grid.muuri > custom-dashboard-grid-item:nth-child(3) > div > custom-dashboard-grid-item-content > div > div > div > header > div > div",
                web_driver)

            self.explicitWait('#main-content > fab-icon > message-indicator > png-badge > ng-transclude > ng-transclude > div',
                         web_driver)
            # Hide question mark button
            web_driver.execute_script(
                "document.querySelector('#main-content > fab-icon > message-indicator > png-badge > ng-transclude > ng-transclude > div').style.visibility = 'hidden';",
                web_driver)
            print("Login Complete")
        except Exception as e:
            print("Exception in Login: " + str(e))


    @pytest.fixture(name="eyes", scope="function")
    def set_up(self, runner):
        eyes = Eyes(runner)
        # You can get your api key from the Applitools dashboard
        eyes.configure.set_api_key(os.environ["APPLITOOLS_API_KEY"])

        # create a new batch info instance and set it to the configuration
        eyes.configure.set_batch(BatchInfo("Dev Training Module - ROBOT"))
        eyes.configure.set_layout_breakpoints(True)

        # TODO ensure this is uncommented
        eyes.configure.set_server_url("https://paychexeyes.applitools.com/")
        # Add browsers with different viewports
        # Add mobile emulation devices in Portrait mode
        (
            eyes.configure.add_browser(1000, 800, BrowserType.CHROME),
            eyes.configure.add_browser(1024, 768, BrowserType.FIREFOX),
            eyes.configure.add_device_emulation(DeviceName.iPhone_X),
            eyes.configure.add_device_emulation(DeviceName.iPad_Pro)
        )
        yield eyes


    def selectMenuButton(self):
        try:
            web_driver = self.get_browser_driver()
            button = web_driver.find_element_by_css_selector(
                "#appContainer > div.top-bar > div.left-nav-trigger-container.visible")
            button.click()
        except NoSuchElementException as e:
            print(e)
            print("Menu button not found.")


    def goToCompanyDetails(self):
        try:
            web_driver = self.get_browser_driver()
            link = web_driver.find_element_by_css_selector(
                "#appContainer > md-sidenav > div.left-nav-content-container > div > div > div.list-wrapper-wrapper > div:nth-child(1) > div:nth-child(6) > div > div > a > span"
            )
            link.click()
            self.explicitWait(
                "#paychex\.app\.company\.profile > div > div.png-error-transclude.full-height > div > div > div.right-column > png-card > div > header > div.png-card-trigger-wrapper", web_driver)
        except Exception as e:
            print(e)


    @pytest.fixture(name="runner", scope="session")
    def runner_setup(self):
        """
        One test runner for all tests. Print test results in the end of execution.
        """
        runner = VisualGridRunner()
        yield runner
        all_test_results = runner.get_all_test_results()
        print(all_test_results)


    @pytest.fixture(name="web_driver", scope="function")
    def driver_setup(self):
        chrome_options = Options()
        chrome_options.headless = HEADLESS

        # Create a new chrome web driver
        web_driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
        # Chrome(ChromeDriverManager(version="99.0.4844.51").install(), options=chrome_options)

        # This is just a setting that sets the time for waiting for elements to be 10s
        web_driver.implicitly_wait(10)
        yield web_driver

        web_driver.quit()


    def test_ultra_fast(self,web_driver, eyes):
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
            self.login(self,web_driver, eyes)
            print("Wait....")
            time.sleep(10)
            print("Checking Main page....")

            eyes.check("Dashboard Region",
                       Target.region("#appContainer").fully())

            self.selectMenuButton(web_driver, eyes)
            self.goToCompanyDetails(web_driver)
            time.sleep(4)
            eyes.check("Company Details",
                       Target.region("#appContainer").fully())

            eyes.close_async()
        except Exception as e:
            eyes.abort_async()
            print(e)
