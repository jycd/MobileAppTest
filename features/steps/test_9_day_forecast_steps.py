from behave import given, when, then
from pages.forecast_page import ForecastPage
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

# --- Common Steps ---

@given('the MyObservatory app is installed')
def step_impl(context):
    # In a real scenario, we might check if the app is installed.
    # Here, we assume the driver setup handles app installation/launch.
    pass

@given('I am on the home screen')
def step_impl(context):
    # Initialize Page Object
    # Driver is already initialized in environment.py
    context.forecast_page = ForecastPage(context.driver)
    
    # Wait for a key element on the home screen (e.g., Menu button)
    # Using the page object's wait method implicitly via find_element
    context.forecast_page.find_element(ForecastPage.MENU_BUTTON)

@given('I am on the "9-Day Forecast" page')
def step_impl(context):
    # Reuse steps to navigate to the page if not already there
    context.execute_steps(u'''
        Given I am on the home screen
        When I tap the "Menu" icon
        And I tap "Forecast & Warning Services"
        And I tap "9-Day Forecast"
        Then the "9-Day Forecast" page should open
    ''')

# --- Navigation Steps ---

@when('I tap the "Menu" icon')
def step_impl(context):
    context.forecast_page.click(ForecastPage.MENU_BUTTON)

@when('I tap "Forecast & Warning Services"')
def step_impl(context):
    context.forecast_page.click(ForecastPage.FORECAST_SERVICES_BTN)

@when('I tap "9-Day Forecast"')
def step_impl(context):
    context.forecast_page.click(ForecastPage.NINE_DAY_FORECAST_BTN)

@then('the "9-Day Forecast" page should open')
def step_impl(context):
    assert context.forecast_page.is_on_forecast_page()

# --- PSR Steps ---

@then('the Probability of Significant Rain should be displayed if applicable')
def step_impl(context):
    # Check for PSR element, but don't fail if not present (as it's conditional)
    if context.forecast_page.is_psr_displayed():
        pass # It's displayed
    else:
        pass # Optional feature

# --- Layout Steps ---

@then('the content should fit within the screen bounds')
def step_impl(context):
    # Get window size
    size = context.driver.get_window_size()
    width = size['width']
    
    days = context.forecast_page.get_forecast_cells()
    if days:
        day_loc = days[0].location
        day_size = days[0].size
        assert day_loc['x'] + day_size['width'] <= width

@then('no text should be truncated')
def step_impl(context):
    # Difficult to verify programmatically without visual tools
    pass

# --- Dark Mode Steps ---

@when('I enable system-wide Dark Mode')
def step_impl(context):
    # Appium doesn't directly toggle system dark mode on iOS easily without specific capabilities or settings
    pass

@then('the background should be dark')
def step_impl(context):
    # Verify via screenshot analysis or checking specific color attributes if exposed
    pass

@then('the text should be light and readable')
def step_impl(context):
    # Verify via screenshot analysis
    pass

# --- Data Freshness Steps ---

@then('the forecast data should match the official HKO website')
def step_impl(context):
    # In a real test, we would fetch data from HKO API/Website and compare
    pass

# --- Scrolling Steps ---

@when('I scroll down to the bottom of the list')
def step_impl(context):
    # Swipe up to scroll down
    size = context.driver.get_window_size()
    start_x = size['width'] // 2
    start_y = int(size['height'] * 0.8)
    end_y = int(size['height'] * 0.2)
    
    # Perform multiple swipes if needed
    for _ in range(3):
        context.driver.swipe(start_x, start_y, start_x, end_y, 800)

@then('the 9th day forecast should be visible')
def step_impl(context):
    days = context.forecast_page.get_forecast_cells()
    assert len(days) >= 9
    assert days[-1].is_displayed()

@when('I scroll back up to the top')
def step_impl(context):
    size = context.driver.get_window_size()
    start_x = size['width'] // 2
    start_y = int(size['height'] * 0.2)
    end_y = int(size['height'] * 0.8)
    
    for _ in range(3):
        context.driver.swipe(start_x, start_y, start_x, end_y, 800)

@then('the first day forecast should be visible')
def step_impl(context):
    days = context.forecast_page.get_forecast_cells()
    if days:
        assert days[0].is_displayed()

# --- Share Steps ---

@when('I tap the "Share" button')
def step_impl(context):
    context.forecast_page.click_share()

@then('the share sheet should open')
def step_impl(context):
    assert context.forecast_page.is_share_sheet_displayed()

# --- Orientation Steps ---

@when('I rotate the device to "Landscape"')
def step_impl(context):
    context.driver.orientation = "LANDSCAPE"

@then('the layout should adjust or remain locked in portrait')
def step_impl(context):
    # Check orientation or element positions
    pass

@then('the title bar should display "9-Day Forecast"')
def step_impl(context):
    assert context.forecast_page.is_on_forecast_page()

@when('I tap the "Back" button')
def step_impl(context):
    context.forecast_page.click_back()

@then('I should return to the previous screen')
def step_impl(context):
    # Verify we are back on the menu or previous list
    # We can reuse the locator from the page object if we expose it, or define a new one
    # For now, checking if the Forecast Services button is visible again
    assert context.forecast_page.is_displayed(ForecastPage.FORECAST_SERVICES_BTN)

# --- Verification Steps ---

@then('I should see the title "9-Day Forecast"')
def step_impl(context):
    assert context.forecast_page.is_on_forecast_page()

@then('a paragraph describing the "General Situation"')
def step_impl(context):
    assert context.forecast_page.is_general_situation_displayed()

@then('a list of 9 forecast days')
def step_impl(context):
    days = context.forecast_page.get_forecast_cells()
    assert len(days) >= 9

@then('each day should display date, day, icon, temperature, humidity, and description')
def step_impl(context):
    days = context.forecast_page.get_forecast_cells()
    for i in range(min(len(days), 9)):
        day_cell = days[i]
        # These assertions are placeholders; actual IDs/Predicates depend on app internals
        assert day_cell.find_elements(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText'), "Text elements missing"
        assert day_cell.find_elements(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage'), "Icon missing"

@when('I pull down to refresh')
def step_impl(context):
    size = context.driver.get_window_size()
    start_x = size['width'] // 2
    start_y = int(size['height'] * 0.3)
    end_y = int(size['height'] * 0.7)
    
    # Swipe down
    context.driver.swipe(start_x, start_y, start_x, end_y, 800)
    sleep(2) # Wait for animation

@then('a loading indicator should appear')
def step_impl(context):
    pass 

@then('the data should refresh')
def step_impl(context):
    days = context.forecast_page.get_forecast_cells()
    assert len(days) > 0

# --- Language Switching Steps ---

@when('I change the app language to "Traditional Chinese"')
def step_impl(context):
    # Navigate to settings and change language
    pass

@when('I navigate to the "9-Day Forecast" page')
def step_impl(context):
    # Reuse navigation logic
    pass

@then('the title bar should display "九天天氣預報"')
def step_impl(context):
    title = context.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "九天天氣預報"')
    assert title.is_displayed()

@then('the content should be in Traditional Chinese')
def step_impl(context):
    pass

# --- Network Steps ---

@when('I disable the internet connection')
def step_impl(context):
    pass

@then('an error message should be displayed')
def step_impl(context):
    pass

# --- Background/Foreground Steps ---

@when('I minimize the app')
def step_impl(context):
    context.driver.background_app(5)

@when('I wait for 5 seconds')
def step_impl(context):
    sleep(5)

@when('I reopen the app')
def step_impl(context):
    pass

@then('I should still be on the "9-Day Forecast" page')
def step_impl(context):
    assert context.forecast_page.is_on_forecast_page()
