package com.applitools.quickstarts;

import com.applitools.eyes.BatchInfo;
import com.applitools.eyes.RectangleSize;
import com.applitools.eyes.TestResultsSummary;
import com.applitools.eyes.selenium.BrowserType;
import com.applitools.eyes.selenium.Configuration;
import com.applitools.eyes.selenium.Eyes;
import com.applitools.eyes.selenium.fluent.Target;
import com.applitools.eyes.visualgrid.model.DeviceName;
import com.applitools.eyes.visualgrid.model.ScreenOrientation;
import com.applitools.eyes.visualgrid.services.VisualGridRunner;
import com.applitools.eyes.visualgrid.services.RunnerOptions;
import com.helger.commons.datetime.PDTWebDateHelper;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.concurrent.TimeUnit;

/**
 * Unit test for simple App.
 */
public class AppTest {

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
		WebDriverWait wait = new WebDriverWait(driver, timeout);
		wait.until(condition);
	}

	public static void main(String[] args) {
		// Create a new chrome web driver
		WebDriver webDriver = new ChromeDriver(new ChromeOptions().setHeadless(getCI()));

		// Create a runner with concurrency of 5
		VisualGridRunner runner = new VisualGridRunner(new RunnerOptions().testConcurrency(5));

		// Create Eyes object with the runner, meaning it'll be a Visual Grid eyes.
		Eyes eyes = new Eyes(runner);

		setUp(eyes);

		try {
			// ⭐️ Note to see visual bugs, run the test using the above URL for the 1st run.
			// but then change the above URL to https://demo.applitools.com/index_v2.html
			// (for the 2nd run)
			ultraFastTest(webDriver, eyes);

		} finally {
			tearDown(webDriver, runner);
		}

	}

	public static boolean getCI() {
		String env = System.getenv("CI");
		return Boolean.parseBoolean(env);
	}

	public static void setUp(Eyes eyes) {

		// Initialize eyes Configuration
		Configuration config = eyes.getConfiguration();

		// You can get your api key from the Applitools dashboard
		config.setApiKey(System.getenv("APPLITOOLS_API_KEY"));

		// create a new batch info instance and set it to the configuration
		config.setBatch(new BatchInfo("Paychex Java"));

		// Add browsers with different viewports
		config.addBrowser(800, 600, BrowserType.CHROME);
		config.addBrowser(700, 500, BrowserType.FIREFOX);
		config.addBrowser(1600, 1200, BrowserType.IE_11);
		config.addBrowser(1024, 768, BrowserType.EDGE_CHROMIUM);
		config.addBrowser(800, 600, BrowserType.SAFARI);

		// Add mobile emulation devices in Portrait mode
		config.addDeviceEmulation(DeviceName.iPhone_X, ScreenOrientation.PORTRAIT);
		config.addDeviceEmulation(DeviceName.Pixel_2, ScreenOrientation.PORTRAIT);

		// Set the configuration object to eyes
		eyes.setConfiguration(config);

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

	public static void ultraFastTest(WebDriver webDriver, Eyes eyes) {

		try {
			String url ="https://myappsimpn.paychex.com/" ;
			//"https://demo.applitools.com";
			// Navigate to the url we want to test
			webDriver.get(url);

			// Call Open on eyes to initialize a test session
			eyes.open(webDriver, "Paychex Flex", "Java Paychex Flex", new RectangleSize(800, 600));

			// check the login page with fluent api, see more info here
			// https://applitools.com/docs/topics/sdk/the-eyes-sdk-check-fluent-api.html

			JavascriptExecutor executor;
			executor = (JavascriptExecutor) webDriver;
			// executor.executeScript("document.querySelector('body > div > div > form > div.buttons-w > div:nth-child(3) > a:nth-child(3)').style.marginLeft = '80px'");

			System.out.println("Logging in");
			login(webDriver, eyes);
			System.out.println("Checking Window");
			eyes.check(Target.window().withName("Login"));
			//eyes.check(Target.window().withName("Dashboard"));

			//webDriver.findElement(By.id("log-in")).click();

			// Check the app page
			//eyes.check(Target.window().fully().withName("App page"));

			// Call Close on eyes to let the server know it should display the results
			eyes.closeAsync();

		} finally  {
			eyes.abortAsync();
		}

	}

	private static void tearDown(WebDriver webDriver, VisualGridRunner runner) {
		// Close the browser
		webDriver.quit();

		// find visual differences
		//TestResultsSummary allTestResults = runner.getAllTestResults(true);
		//System.out.println(allTestResults);
	}

}
