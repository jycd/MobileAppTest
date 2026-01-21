from behave import given, when, then
from utils.appium_driver import get_driver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the MyObservatory app is installed')
def step_impl(context):
    # Assume app is installed on device
    pass

@given('I am on the home screen')
def step_impl(context):
    context.driver = get_driver()
    # Wait for home screen to load (adjust accessibility_id as needed)
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Menu"))
    )

@when('I tap the "Menu" icon')
def step_impl(context):
    menu = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Menu"))
    )
    menu.click()

@when('I tap "Forecast & Warning Services"')
def step_impl(context):
    forecast_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.IOS_PREDICATE, 'label == "Forecast & Warning Services"'))
    )
    forecast_btn.click()

@when('I tap "9-Day Forecast"')
def step_impl(context):
    forecast9_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.IOS_PREDICATE, 'label == "9-Day Forecast"'))
    )
    forecast9_btn.click()

@then('the "9-Day Forecast" page should open')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((MobileBy.IOS_PREDICATE, 'label == "9-Day Forecast"'))
    )

@then('the title bar should display "9-Day Forecast"')
def step_impl(context):
    title = context.driver.find_element(MobileBy.IOS_PREDICATE, 'label == "9-Day Forecast"')
    assert title.is_displayed()

@when('I tap the "Back" button')
def step_impl(context):
    back_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Back"))
    )
    back_btn.click()

@then('I should return to the previous screen')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((MobileBy.IOS_PREDICATE, 'label == "Forecast & Warning Services"'))
    )

@then('I should see the title "9-Day Forecast"')
def step_impl(context):
    title = context.driver.find_element(MobileBy.IOS_PREDICATE, 'label == "9-Day Forecast"')
    assert title.is_displayed()

@then('a paragraph describing the "General Situation"')
def step_impl(context):
    # Adjust predicate for the actual element
    general_situation = context.driver.find_element(MobileBy.IOS_PREDICATE, 'label CONTAINS "General Situation"')
    assert general_situation.is_displayed()

@then('a list of 9 forecast days')
def step_impl(context):
    # Adjust class name or identifier as needed
    days = context.driver.find_elements(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell')
    assert len(days) == 9

@then('each day should display date, day, icon, temperature, humidity, and description')
def step_impl(context):
    days = context.driver.find_elements(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell')
    for day in days:
        # Example: check for sub-elements, adjust as needed
        assert day.find_element(MobileBy.IOS_PREDICATE, 'label CONTAINS "°C"')
        assert day.find_element(MobileBy.IOS_PREDICATE, 'label CONTAINS "%"')
        assert day.find_element(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage')
        assert day.find_element(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText')

@when('I pull down to refresh')
def step_impl(context):
    # Get list element and perform swipe down
    size = context.driver.get_window_size()
    start_x = size['width'] // 2
    start_y = int(size['height'] * 0.3)
    end_y = int(size['height'] * 0.7)
    context.driver.swipe(start_x, start_y, start_x, end_y, 800)
    sleep(2)

@then('a loading indicator should appear')
def step_impl(context):
    # Adjust for actual loading indicator
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((MobileBy.IOS_PREDICATE, 'label CONTAINS "Loading"'))
    )

@then('the data should refresh')
def step_impl(context):
    # Optionally check for updated timestamp or data
    refreshed = context.driver.find_element(MobileBy.IOS_PREDICATE, 'label CONTAINS "Updated"')
    assert refreshed.is_displayed()
