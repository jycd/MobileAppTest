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
