package com.applitools.example;

import com.applitools.eyes.BatchInfo;
import com.applitools.eyes.RectangleSize;
import com.applitools.eyes.TestResultsSummary;
import com.applitools.eyes.selenium.BrowserType;
import com.applitools.eyes.selenium.Configuration;
import com.applitools.eyes.selenium.Eyes;
import com.applitools.eyes.selenium.fluent.Target;
import com.applitools.eyes.visualgrid.model.DeviceName;
import com.applitools.eyes.visualgrid.model.ScreenOrientation;
import com.applitools.eyes.visualgrid.services.RunnerOptions;
import com.applitools.eyes.visualgrid.services.VisualGridRunner;
import org.junit.jupiter.api.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.concurrent.TimeUnit;

public class Applitools_Activity {
    // This JUnit test case class contains everything needed to run a full visual test against the ACME bank site.
    // It runs the test once locally,
    // and then it performs cross-browser testing against multiple unique browsers in Applitools Ultrafast Grid.

    // Test control inputs to read once and share for all tests
    private static String applitoolsApiKey;
    private static boolean headless = true;

    // Applitools objects to share for all tests
    private static BatchInfo batch;
    private static Configuration config;
    private static VisualGridRunner runner;

    // Test-specific objects
    private WebDriver driver;
    private Eyes eyes;

    private static final CharSequence  username = "Applit465856618";
    private static final CharSequence password = "Test1234";

    protected static Boolean waitForIsDisplayed(By locator, WebDriver driver, Integer... timeout) {
        try {
            waitFor(driver, ExpectedConditions.visibilityOfElementLocated(locator),
                    (timeout.length > 0 ? timeout[0] : null));
        } catch (org.openqa.selenium.TimeoutException exception) {
            System.out.println("Could not find locator: " + locator.toString());
            return false;
        }
        return true;
    }

    private static void waitFor(WebDriver driver, ExpectedCondition<WebElement> condition, Integer timeout) {
        timeout = timeout != null ? timeout : 5;
        WebDriverWait wait = new WebDriverWait(driver, (Duration.ofSeconds(timeout)));
        wait.until(condition);
    }


    public static void login(WebDriver driver, Eyes eyes) {
        try {
            // Username field, next button
            //wait(5000);
            driver.switchTo().frame("login");
            waitForIsDisplayed(By.cssSelector("div.col-sm-6:nth-child(3) > button:nth-child(1)"), driver);
            WebElement usernameField = driver.findElement(By.id("USER"));
            usernameField.sendKeys(username);
            driver.findElement(By.cssSelector("div.col-sm-6:nth-child(3) > button:nth-child(1)")).click();
            waitForIsDisplayed(By.cssSelector("#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)"), driver);
            WebElement nextButton = driver.findElement(By.cssSelector("#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)"));
            nextButton.click();

            waitForIsDisplayed(By.className("control-label"), driver);
            String secQuestion = driver.findElement(By.className("control-label")).getText();
            String[] answerSplit = secQuestion.split("[' '|?]");
            String answer = answerSplit[answerSplit.length - 1];
            driver.findElement(By.id("answer")).sendKeys(answer);
            driver.findElement(By.cssSelector("#appPlaceHolder > div.ng-scope > div > form > div:nth-child(2) > div > div > button:nth-child(2)")).click();

            waitForIsDisplayed(By.cssSelector("#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)"), driver);
            waitForIsDisplayed(By.className("form-control"), driver);
            driver.findElement(By.className("form-control")).sendKeys(password);
            driver.findElement(By.cssSelector("#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)")).click();
            driver.switchTo().defaultContent();

            TimeUnit.SECONDS.sleep(5);

        }
        catch (Exception ex) {
            System.out.println("Exception in login: " + ex.getMessage());
        }
    }



    @BeforeAll
    public static void setUpConfigAndRunner() {
        // This method sets up the configuration for running visual tests in the Ultrafast Grid.
        // The configuration is shared by all tests in a test suite, so it belongs in a `BeforeAll` method.
        // If you have more than one test class, then you should abstract this configuration to avoid duplication.

        // Read the Applitools API key from an environment variable.
        // To find your Applitools API key:
        // https://applitools.com/tutorials/getting-started/setting-up-your-environment.html
        applitoolsApiKey = System.getenv("APPLITOOLS_API_KEY");

        // Read the headless mode setting from an environment variable.
        // Use headless mode for Continuous Integration (CI) execution.
        // Use headed mode for local development.
        //headless = Boolean.parseBoolean(System.getenv().getOrDefault("HEADLESS", "true"));

        // Create the runner for the Ultrafast Grid.
        // Concurrency refers to the number of visual checkpoints Applitools will perform in parallel.
        // Warning: If you have a free account, then concurrency will be limited to 1.
        runner = new VisualGridRunner(new RunnerOptions().testConcurrency(5));

        // Create a new batch for tests.
        // A batch is the collection of visual checkpoints for a test suite.
        // Batches are displayed in the dashboard, so use meaningful names.
        batch = new BatchInfo("Dev Training Module - Java");

        // Create a configuration for Applitools Eyes.
        config = new Configuration();

        // Set the Applitools API key so test results are uploaded to your account.
        // If you don't explicitly set the API key with this call,
        // then the SDK will automatically read the `APPLITOOLS_API_KEY` environment variable to fetch it.
        config.setApiKey(applitoolsApiKey);

        config.setServerUrl("https://service-outbound-par.paychex.com/pxt-applitools");

        config.setLayoutBreakpoints(true);

        // Set the batch for the config.
        config.setBatch(batch);

        // Add 3 desktop browsers with different viewports for cross-browser testing in the Ultrafast Grid.
        // Other browsers are also available, like Edge and IE.
        config.addBrowser(800, 600, BrowserType.CHROME);
        config.addBrowser(1600, 1200, BrowserType.FIREFOX);
        config.addBrowser(1024, 768, BrowserType.SAFARI);

        // Add 2 mobile emulation devices with different orientations for cross-browser testing in the Ultrafast Grid.
        // Other mobile devices are available, including iOS.
        config.addDeviceEmulation(DeviceName.Pixel_2, ScreenOrientation.PORTRAIT);
        config.addDeviceEmulation(DeviceName.Nexus_10, ScreenOrientation.LANDSCAPE);
    }

    @BeforeEach
    public void openBrowserAndEyes(TestInfo testInfo) {
        // This method sets up each test with its own ChromeDriver and Applitools Eyes objects.

        // Open the browser with the ChromeDriver instance.
        // Even though this test will run visual checkpoints on different browsers in the Ultrafast Grid,
        // it still needs to run the test one time locally to capture snapshots.
        driver = new ChromeDriver(new ChromeOptions().setHeadless(headless));

        // Set an implicit wait of 10 seconds.
        // For larger projects, use explicit waits for better control.
        // https://www.selenium.dev/documentation/webdriver/waits/
        // The following call works for Selenium 4:
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

        // If you are using Selenium 3, use the following call instead:
        // driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        // Create the Applitools Eyes object connected to the VisualGridRunner and set its configuration.
        eyes = new Eyes(runner);
        eyes.setConfiguration(config);

        // Open Eyes to start visual testing.
        // It is a recommended practice to set all four inputs:
        eyes.open(
                driver,                                         // WebDriver object to "watch"
                "Paychex Flex",                            // The name of the app under test
                testInfo.getDisplayName(),                      // The name of the test case
                new RectangleSize(1024, 768));    // The viewport size for the local browser
    }

    @Test
    public void ultraFastTest() {

        try {
            String url ="https://myappsimpn.paychex.com/" ;
            driver.get(url);

            // Call Open on eyes to initialize a test session
            //eyes.open(driver, "Paychex Flex", "Java Paychex Flex", new RectangleSize(800, 600));

            // check the login page with fluent api, see more info here
            // https://applitools.com/docs/topics/sdk/the-eyes-sdk-check-fluent-api.html

            System.out.println("Logging in...");
            login(driver, eyes);
            System.out.println("Checking Dashboard...");

            //TODO create eyes checks (with Target.region on the #appContainer for the dashboard

            //This code nagivates to the company page
            driver.findElement(By.cssSelector("#appContainer > div.top-bar > div.left-nav-trigger-container.visible")).click();
            driver.findElement(By.cssSelector("#appContainer > md-sidenav > div.left-nav-content-container > div > div > div.list-wrapper-wrapper > div:nth-child(1) > div:nth-child(6) > div > div > a > span")).click();

            //TODO add another check here on the #appContainer

        } catch (Exception exception) {
            eyes.abortAsync();
        }
    }

    @AfterEach
    public void cleanUpTest() {

        // Quit the WebDriver instance.
        driver.quit();

        // Close Eyes to tell the server it should display the results.
        eyes.closeAsync();

        // Warning: `eyes.closeAsync()` will NOT wait for visual checkpoints to complete.
        // You will need to check the Applitools dashboard for visual results per checkpoint.
        // Note that "unresolved" and "failed" visual checkpoints will not cause the JUnit test to fail.

        // If you want the JUnit test to wait synchronously for all checkpoints to complete, then use `eyes.close()`.
        // If any checkpoints are unresolved or failed, then `eyes.close()` will make the JUnit test fail.
    }

    @AfterAll
    public static void printResults() {

        // Close the batch and report visual differences to the console.
        // Note that it forces JUnit to wait synchronously for all visual checkpoints to complete.
        TestResultsSummary allTestResults = runner.getAllTestResults();
        System.out.println(allTestResults);
    }
}
