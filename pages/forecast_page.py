from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ForecastPage(BasePage):
    # Locators
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Menu")
    FORECAST_SERVICES_BTN = (AppiumBy.IOS_PREDICATE, 'label == "Forecast & Warning Services"')
    NINE_DAY_FORECAST_BTN = (AppiumBy.IOS_PREDICATE, 'label == "9-Day Forecast"')
    PAGE_TITLE = (AppiumBy.IOS_PREDICATE, 'label == "9-Day Forecast"')
    PSR_LABEL = (AppiumBy.IOS_PREDICATE, 'label CONTAINS "Probability"')
    GENERAL_SITUATION = (AppiumBy.IOS_PREDICATE, 'label CONTAINS "General Situation"')
    FORECAST_CELLS = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell')
    SHARE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Share")
    SHARE_SHEET = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSheet')
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Back")

    def navigate_to_forecast(self):
        self.click(self.MENU_BUTTON)
        self.click(self.FORECAST_SERVICES_BTN)
        self.click(self.NINE_DAY_FORECAST_BTN)

    def is_on_forecast_page(self):
        return self.is_displayed(self.PAGE_TITLE)

    def get_forecast_cells(self):
        return self.driver.find_elements(*self.FORECAST_CELLS)

    def is_psr_displayed(self):
        return self.is_displayed(self.PSR_LABEL)

    def is_general_situation_displayed(self):
        return self.is_displayed(self.GENERAL_SITUATION)

    def click_share(self):
        self.click(self.SHARE_BUTTON)

    def is_share_sheet_displayed(self):
        return self.is_displayed(self.SHARE_SHEET)

    def click_back(self):
        self.click(self.BACK_BUTTON)
