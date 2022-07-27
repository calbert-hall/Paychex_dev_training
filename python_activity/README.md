# Paychex Dev Training Module: Eyes Python Selenium Ultrafast Ggit rid 

### 1. Pre-requisites:

1. Python 3 is installed on your machine.  [Install Python 3.](https://realpython.com/installing-python/) 
2. Package manager pip is installed on your machine.  [Install pip](https://pip.pypa.io/en/stable/installing/)
3. Chrome browser is installed on your machine. [Install Chrome browser](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en&oco=0)  
4. Chrome Webdriver is on your machine and is in the environment variable PATH. Here are some resources from the internet that'll help you.
   * [Download Chrome Webdriver](https://chromedriver.chromium.org/downloads), [Read the docs](https://splinter.readthedocs.io/en/0.1/setup-chrome.html), [Stackoverflow](https://stackoverflow.com/questions/38081021/using-selenium-on-mac-chrome), [Youtube](https://www.youtube.com/watch?time_continue=182&v=dz59GsdvUF8)
5. Git is installed on your machine. [Install git](https://www.atlassian.com/git/tutorials/install-git)
6. If you want to run example from IDE, install any IDE for Python (We recommend and will be using [PyCharm](https://www.jetbrains.com/pycharm/download/) )

### 2. Run the Initial Test 
1. Install requirements `pip install -r requirements.txt`
2. Open `getting_started.py ` and set your ApiKey in string `.set_api_key('...')`
3. Change the Applitools batch name in the `set_up` method to your team name. If you're not sure, just put the breakout team leader's name.  
4. Run `getting_started.py` by calling `python getting_started.py` 

For additional info, see our official documentation here: https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python_sdk4.html

### 3. Dev Training Module Activities: Selenium Python
1. Open `applitools_activity.py` and set the API key and batch name as in steps 2 and 3 from #2.
2. Create an eyes.check call on the main Paychex Flex dashboard after the login window. 
3. Run `applitools_activity.py` by calling `pytest applitools_activity.py`. *Note, you may need to run multiple times for the test to cache properly to capture the images*. 
4. Create a layout region from the Applitools dashboard over the messages icon in the blue header on your tests. Enable Auto-maintenance to do this more quickly!
5. Use the link from the menu to go to the company details, then take a screenshot of the company details page! 
*Hint: I've made several helper functions to make this an easy process, please use them!*
6. Place an Ignore region on the "Company Logo" portion of the company details page. 
7. Implement a *coded region* in one of your `eyes.check` calls. 
8. Navigate through the tabs on the company details page, and use eyes.check to capture these pages as well. 
9. If you still have time, ask Casey for any additional tasks. 

Troubleshooting

- Try toggling the HEADLESS setting at the top of the file. This tells chromedriver whether to run in headless mode. 
  This can be useful if you get errors related to viewport size. 
- If you don't get perfect results initially, try running again. Oftentimes once the initial process is cached, the 
testing goes more quicky and effectively.
  
- If you're still not seeing everything load and are seeing selector related messages, increase the EXPLICIT_WAIT_TIME. 
