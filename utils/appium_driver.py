from appium import webdriver

def get_driver():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '15.0',
        'deviceName': 'iPhone Simulator',
        'app': '/path/to/MyObservatory.app',
        'automationName': 'XCUITest',
        'noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
