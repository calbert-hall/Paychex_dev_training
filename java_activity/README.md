# Applitools Example: Selenium Java JUnit with the Ultrafast Grid

This is the example project for the [Selenium Java JUnit tutorial](https://applitools.com/tutorials/selenium-java.html).
It shows how to start automating visual tests
with [Applitools Eyes](https://applitools.com/platform/eyes/)
and the [Ultrafast Grid](https://applitools.com/platform/ultrafast-grid/)
using [Selenium WebDriver](https://www.selenium.dev/) in Java.

It uses:

* [Java](https://www.java.com/) as the programming language
* [Selenium WebDriver](https://www.selenium.dev/) for browser automation
* [Google Chrome](https://www.google.com/chrome/downloads/) as the local browser for testing
* [Apache Maven](https://maven.apache.org/index.html) for dependency management
* [JUnit 5](https://junit.org/junit5/) as the core test framework
* [Applitools Eyes](https://applitools.com/platform/eyes/) for visual testing
* [Applitools Ultrafast Grid](https://applitools.com/platform/ultrafast-grid/) for cross-browser execution

To run this example project, you'll need:

1. An [Applitools account](https://auth.applitools.com/users/register), which you can register for free.
2. The [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/downloads/), version 8 or higher.
3. A good Java editor, such as [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/).
4. [Apache Maven](https://maven.apache.org/download.cgi) (typically bundled with IDEs).
5. An up-to-date version of [Google Chrome](https://www.google.com/chrome/downloads/).
6. A corresponding version of [ChromeDriver](https://chromedriver.chromium.org/downloads).

The main test case is [`AcmeBankTests.java`](src/test/java/com/applitools/example/AcmeBankTests.java).

To execute tests, set the `APPLITOOLS_API_KEY` environment variable
to your [account's API key](https://applitools.com/tutorials/getting-started/setting-up-your-environment.html),
and then run:

```
mvn test
```

**For full instructions on running this project, take our
[Selenium Java JUnit tutorial](https://applitools.com/tutorials/selenium-java.html)!**


# Paychex Dev Training Module
- See above to run the sample project to ensure you're set up correctly
- See TODOs and further directions in the General readme
- If you have extra time, try designing an eyes wrapper function or look to try to structure the code in a more scalable
framework. 


### Troubleshooting

- Try toggling the HEADLESS setting at the top of the file. This tells chromedriver whether to run in headless mode.
  This can be useful if you get errors related to viewport size.
- If you don't get perfect results initially, try running again. Oftentimes once the initial process is cached, the
  testing goes more quicky and effectively.

- If you're still not seeing everything load and are seeing selector related messages, increase the EXPLICIT_WAIT_TIME.


