import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import os

APPLIFASHIONV1 = "https://demo.applitools.com/gridHackathonV1.html"
APPLIFASHIONVDEV = "https://demo.applitools.com/tlcHackathonDev.html"
APPLIFASHIONV2 = "https://demo.applitools.com/gridHackathonV2.html"

#TODO set Dyanmic content
DYNAMIC_CONTENT = False 

#TODO change the ENV_URL to change which environment is use
ENV_URL = APPLIFASHIONV1

#Useful selectors
blackColorFilter = "SPAN__checkmark__107" #id
filterBtn = "filterBtn" #id
blackShoesImage= "/html/body/div[1]/main/div/div/div/div[4]/div[1]/div/figure/a/img" #xpath

from applitools.selenium import (
    logger,
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)


def set_up(eyes):

    # You can get your api key from the Applitools dashboard
    eyes.configure.set_api_key(os.environ["APPLITOOLS_API_KEY"])

    # create a new batch info instance and set it to the configuration
    eyes.configure.set_batch(BatchInfo("Hackathon Batch - Python"))

    # Add browsers with different viewports
    # Add mobile emulation devices in Portrait mode
    (
        eyes.configure.add_browser(1200, 800, BrowserType.CHROME)
        #TODO add browsers + viewports
            )


def ultra_fast_test(web_driver, eyes):
    try:
        # Navigate to the url we want to test
        web_driver.get(ENV_URL)

        # Call Open on eyes to initialize a test session
        eyes.open(
            web_driver, "Hackathon", "[Your Team] : Applifashion Filter Workflow Test'", {"width": 1200, "height": 800}
        )

        if DYNAMIC_CONTENT :
            web_driver.execute_script("document.querySelectorAll('h3').forEach(function(noFade) { noFade.innerHTML = Math.random().toString(36);})")


        #TODO your code here!






        # Call Close on eyes to let the server know it should display the results
        eyes.close_async(False)
    except Exception as e:
        eyes.abort_async()
        print(e)


def tear_down(web_driver, runner):
    # Close the browser
    web_driver.quit()

    # we pass false to this method to suppress the exception that is thrown if we
    # find visual differences
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


# Create a new chrome web driver
web_driver = Chrome(ChromeDriverManager().install())

# Create a runner with concurrency of 1
runner = VisualGridRunner(1)

# Create Eyes object with the runner, meaning it'll be a Visual Grid eyes.
eyes = Eyes(runner)

set_up(eyes)

try:
    # ⭐️ Note to see visual bugs, run the test using the above URL for the 1st run.
    # but then change the above URL to https://demo.applitools.com/index_v2.html
    # (for the 2nd run)
    ultra_fast_test(web_driver, eyes)
finally:
    tear_down(web_driver, runner)
