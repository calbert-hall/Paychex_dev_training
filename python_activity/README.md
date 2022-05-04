# Paychex Hackathon: Eyes Python Selenium Ultrafastgrid 

### Pre-requisites:

1. Python 3 is installed on your machine.  [Install Python 3.](https://realpython.com/installing-python/) 
2. Package manager pip is installed on your machine.  [Install pip](https://pip.pypa.io/en/stable/installing/)
3. Chrome browser is installed on your machine. [Install Chrome browser](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en&oco=0)  
4. Chrome Webdriver is on your machine and is in the environment variable PATH. Here are some resources from the internet that'll help you.
   * [Download Chrome Webdriver](https://chromedriver.chromium.org/downloads), [Read the docs](https://splinter.readthedocs.io/en/0.1/setup-chrome.html), [Stackoverflow](https://stackoverflow.com/questions/38081021/using-selenium-on-mac-chrome), [Youtube](https://www.youtube.com/watch?time_continue=182&v=dz59GsdvUF8)
5. Git is installed on your machine. [Install git](https://www.atlassian.com/git/tutorials/install-git)
6. If you want to run example from IDE, install any IDE for Python (We recommend and will be using [PyCharm](https://www.jetbrains.com/pycharm/download/) )

### Run the Initial Test 
1. Open in any editor file `hackathon.py ` and set your ApiKey in string `.set_api_key('...')`
2. Install requirements `pip install -r requirements.txt`
3. Change the Applitools batch name in the `set_up` method to your team name. If you're not sure, just put the breakout team leader's name.  
4. Run `hackathon.py` by calling `python hackathon.py` 

Read our official documentation here: https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python_sdk4.html

### Hackathon Activities: Selenium Python
1. Ensure you've completed the setup and have changed your Applitools batch name (Step 6).
2. Run `hackathon.py` as shown above. 
3. Create a layout region from the Applitools dashboard over the messages icon in the blue header on your tests. Enable Auto-maintenance to do this more quickly!
4. Use the link from the menu to go to the company details, then take a screenshot of the company details page! 
*Hint: I've made several helper functions to make this an easy process, please use them!*
5. Place an Ignore region on the "Company Logo" portion of the company details page. 
6. If you've done this along with the PDF tester (below), ask Casey for more activities. 

### Hackathon Activities: Image Tester
[Image Tester Documentation](https://help.applitools.com/hc/en-us/articles/360007188551-Image-Tester-Stand-alone-tool-for-images-comparison)

Prerequisites: [You have a Java Runtime Environment installed](https://docs.oracle.com/goldengate/1212/gg-winux/GDRAD/java.htm#BGBFHBEA)
1. Establish baselines on the primary PDF using ImageTester. With a terminal open and ImageTester downloaded, your test run should look similar to this. Note the path to the pdf file after -f will change depending on where your pdf is located. 
`java -jar ImageTester_2.0.0.jar -fn "Payroll [My team name]" -f pdfs/Paychex_Payroll.pdf`
2. Test the changed PDF against the original. *Hint: use -fn to force the tests to have the same name and keep them from establishing separate baselines.*
   
3. Run the test again with the "Layout" match level and observe what happens.  
4. Repeat this process with the Images provided that were taken from the Paychex flex dashboard. (ApplitoolsImage1.png as a baseline, BuggyImage1.png as a second run). 
