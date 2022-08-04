# Paychex Dev Training Module - Applitools Activity

### See individual project Readme files for instructions specific to each SDK. 

Prerequisites: have python/java installed in your environment. 
You can also set your APPLITOOLS_API_KEY as an [environment variable](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html) for addional ease of use. If not you can instead hardcode this into each project. 

### General Instructions 

 1. Open applitools_activity and set the API key and batch name as in steps 2 and 3 from #2.
 2. Create an eyes.check call on the main Paychex Flex dashboard after the login window.
 3. Run applitools_activity. *Note, you may need to run multiple times for the test to    cache properly to capture the images*.
 4. Create a layout region from the Applitools dashboard over the messages icon in the blue header on your tests. Enable Auto-maintenance to do this more quickly!
 5. Use the link from the menu to go to the company details, then take a screenshot of the company details  page!
 *Hint: I've made several helper functions to make this an easy process, please use them!*
 6. Place an Ignore region on the "Company Logo" portion of the company details page.
 7. Implement a *coded region* in one of your `eyes.check` calls.
 8. Navigate through the tabs on the company details page, and use eyes.check to capture these pages as well.
 9. Move on to the ImageTester activity. 
 9. If you still have time, ask Casey for any additional tasks.

 *Troubleshooting*

 - Try toggling the HEADLESS setting at the top of the file. This tells chromedriver whether to run in headless mode.
   This can be useful if you get errors related to viewport size.
 - If you don't get perfect results initially, try running again. Oftentimes once the initial process is cached, the
 testing goes more quicky and effectively.

 - If you're still not seeing everything load and are seeing selector related messages, increase the EXPLICIT_WAIT_TIME.
 - If you need any hints, each project has a solution that you can peek at or run to see expected results. 
