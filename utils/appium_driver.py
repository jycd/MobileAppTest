from appium import webdriver
import os
import json

def get_driver():
    """
    Initializes and returns the Appium driver based on configuration file or environment variables.
    """
    # Load configuration
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.json')
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}, using defaults.")
        config = {}

    # Configuration with defaults (can be overridden by env vars, then config file)
    app_path = os.getenv('APP_PATH', config.get('app_path', '/path/to/MyObservatory.app'))
    platform_name = os.getenv('PLATFORM_NAME', config.get('platform_name', 'iOS'))
    device_name = os.getenv('DEVICE_NAME', config.get('device_name', 'iPhone Simulator'))
    platform_version = os.getenv('PLATFORM_VERSION', config.get('platform_version', '17.2'))
    appium_url = os.getenv('APPIUM_URL', config.get('appium_url', 'http://localhost:4723'))
    new_command_timeout = config.get('new_command_timeout', 300)

    automation_name = config.get('automation_name_ios', 'XCUITest') if platform_name == 'iOS' else config.get('automation_name_android', 'UiAutomator2')

    desired_caps = {
        'platformName': platform_name,
        'platformVersion': platform_version,
        'deviceName': device_name,
        'app': app_path,
        'automationName': automation_name,
        'noReset': True,
        'newCommandTimeout': new_command_timeout
    }

    print(f"Starting Appium driver with caps: {desired_caps}")
    
    try:
        driver = webdriver.Remote(appium_url, desired_caps)
        return driver
    except Exception as e:
        print(f"Failed to initialize Appium driver: {e}")
        raise
