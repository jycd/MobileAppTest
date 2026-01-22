# Project Optimization Plan

## 1. Architecture: Page Object Model (POM)
**Current State:** Step definitions contain direct WebDriver calls and element locators.
**Optimization:** Implement the Page Object Model to separate test logic (steps) from UI interaction logic (pages).
- **Action:** Create a `pages/` directory.
- **Action:** Create `pages/base_page.py` for common methods (wait_for_element, click, etc.).
- **Action:** Create `pages/forecast_page.py` for specific 9-Day Forecast elements and actions.

## 2. Lifecycle Management: Hooks
**Current State:** Driver initialization happens lazily inside a step definition.
**Optimization:** Use Behave's `environment.py` hooks to manage the test lifecycle.
- **Action:** Create `features/environment.py`.
- **Action:** Implement `before_scenario` to initialize the driver.
- **Action:** Implement `after_scenario` to quit the driver and capture screenshots on failure.

## 3. Configuration Management
**Current State:** Configuration is hardcoded in `utils/appium_driver.py` with fallback environment variables.
**Optimization:** Centralize configuration in a dedicated file.
- **Action:** Create `config/config.json` (or `config.yaml`) to store device capabilities, app paths, and timeouts.
- **Action:** Update `utils/appium_driver.py` to load this configuration.

## 4. Reporting
**Current State:** Standard console output.
**Optimization:** Integrate a rich reporting tool.
- **Action:** Add `allure-behave` to `requirements.txt`.
- **Action:** Configure `behave.ini` to use the Allure formatter.

## 5. Code Quality
**Current State:** No visible linting or formatting configuration.
**Optimization:** Enforce coding standards.
- **Action:** Add `pylint` and `black` to `requirements.txt`.
- **Action:** Create a `.gitignore` file to exclude artifacts (venv, reports, etc.).
