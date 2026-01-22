Feature: 9-Day Forecast
  As a user of MyObservatory
  I want to view the 9-Day Forecast
  So that I can plan according to the weather

  Background:
    Given the MyObservatory app is installed
    And I am on the home screen

  Scenario: Navigation to 9-Day Forecast page
    When I tap the "Menu" icon
    And I tap "Forecast & Warning Services"
    And I tap "9-Day Forecast"
    Then the "9-Day Forecast" page should open
    And the title bar should display "9-Day Forecast"

  Scenario: Back navigation from 9-Day Forecast
    Given I am on the "9-Day Forecast" page
    When I tap the "Back" button
    Then I should return to the previous screen

  Scenario: Verify UI elements on 9-Day Forecast page
    Given I am on the "9-Day Forecast" page
    Then I should see the title "9-Day Forecast"
    And a paragraph describing the "General Situation"
    And a list of 9 forecast days
    And each day should display date, day, icon, temperature, humidity, and description

  Scenario: Verify pull-to-refresh functionality
    Given I am on the "9-Day Forecast" page
    When I pull down to refresh
    Then a loading indicator should appear
    And the data should refresh

  Scenario: Verify Language Switching to Traditional Chinese
    Given I am on the home screen
    When I change the app language to "Traditional Chinese"
    And I navigate to the "9-Day Forecast" page
    Then the title bar should display "九天天氣預報"
    And the content should be in Traditional Chinese

  Scenario: Verify behavior with No Internet Connection
    Given I am on the home screen
    When I disable the internet connection
    And I navigate to the "9-Day Forecast" page
    Then an error message should be displayed

  Scenario: Verify App Background/Foreground
    Given I am on the "9-Day Forecast" page
    When I minimize the app
    And I wait for 5 seconds
    And I reopen the app
    Then I should still be on the "9-Day Forecast" page

  Scenario: Verify Probability of Significant Rain (PSR)
    Given I am on the "9-Day Forecast" page
    Then the Probability of Significant Rain should be displayed if applicable

  Scenario: Verify Layout on different screen sizes
    Given I am on the "9-Day Forecast" page
    Then the content should fit within the screen bounds
    And no text should be truncated

  Scenario: Verify Dark Mode Support
    Given I am on the home screen
    When I enable system-wide Dark Mode
    And I navigate to the "9-Day Forecast" page
    Then the background should be dark
    And the text should be light and readable

  Scenario: Verify Data Freshness
    Given I am on the "9-Day Forecast" page
    Then the forecast data should match the official HKO website

  Scenario: Verify Scrolling
    Given I am on the "9-Day Forecast" page
    When I scroll down to the bottom of the list
    Then the 9th day forecast should be visible
    When I scroll back up to the top
    Then the first day forecast should be visible

  Scenario: Verify Share Functionality
    Given I am on the "9-Day Forecast" page
    When I tap the "Share" button
    Then the share sheet should open

  Scenario: Verify Orientation Change
    Given I am on the "9-Day Forecast" page
    When I rotate the device to "Landscape"
    Then the layout should adjust or remain locked in portrait
