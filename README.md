# MyObservatory 9-Day Forecast Test Automation

This project contains automated tests for the "9-Day Forecast" feature of the MyObservatory iOS application using Python, Appium, and Behave (BDD).

## Prerequisites

*   **Python 3.9+**
*   **Appium Server** (v2.0+ recommended)
*   **Xcode** (for iOS Simulator)
*   **MyObservatory.app** build (Simulator build)

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The test execution can be configured using environment variables. The default configuration in `utils/appium_driver.py` targets an iPhone Simulator.

**Environment Variables:**

*   `APP_PATH`: Path to the `.app` file (Default: `/path/to/MyObservatory.app`)
*   `PLATFORM_NAME`: Mobile platform (Default: `iOS`)
*   `DEVICE_NAME`: Device name (Default: `iPhone Simulator`)
*   `PLATFORM_VERSION`: iOS version (Default: `17.2`)
*   `APPIUM_URL`: Appium server URL (Default: `http://localhost:4723`)

## Running Tests

1.  **Start Appium Server:**
    Open a new terminal and run:
    ```bash
    appium
    ```

2.  **Run Tests with Behave:**
    In the project root, run:
    ```bash
    # Run all features
    behave

    # Run specific feature
    behave features/9_day_forecast.feature
    ```

3.  **Generate Allure Report (Optional):**
    To generate and view the Allure test report:
    ```bash
    # Run tests and generate results
    behave -f allure_behave.formatter:AllureFormatter -o allure-results

    # Serve the report
    allure serve allure-results
    ```

## Project Structure

*   `features/`: Contains Gherkin feature files (`.feature`).
*   `features/steps/`: Contains Python step definitions (`.py`).
*   `utils/`: Contains utility scripts like `appium_driver.py`.
*   `requirements.txt`: Python dependencies.
*   `behave.ini`: Behave configuration.

## Test Scenarios

The `features/9_day_forecast.feature` file covers the following scenarios:
1.  Navigation to the 9-Day Forecast page.
2.  Back navigation to the previous screen.
3.  Verification of UI elements (Title, General Situation, Forecast List).
4.  Pull-to-refresh functionality.
5.  Language Switching to Traditional Chinese.
6.  Behavior with No Internet Connection.
7.  App Background/Foreground behavior.
8.  Probability of Significant Rain (PSR) display.
9.  Layout on different screen sizes.
10. Dark Mode Support.
11. Data Freshness verification.
12. Scrolling functionality.
13. Share Functionality.
14. Orientation Change handling.
