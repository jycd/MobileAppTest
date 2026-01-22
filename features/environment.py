from utils.appium_driver import get_driver
import os

def before_scenario(context, scenario):
    """
    Runs before each scenario.
    Initializes the Appium driver and attaches it to the context.
    """
    print(f"Starting scenario: {scenario.name}")
    context.driver = get_driver()

def after_scenario(context, scenario):
    """
    Runs after each scenario.
    Quits the driver and captures a screenshot if the scenario failed.
    """
    if scenario.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        screenshot_name = f"screenshots/{scenario.name.replace(' ', '_')}_failed.png"
        try:
            context.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved to {screenshot_name}")
        except Exception as e:
            print(f"Failed to save screenshot: {e}")

    if hasattr(context, 'driver'):
        print(f"Finishing scenario: {scenario.name}")
        context.driver.quit()
