# Test Cases: MyObservatory - 9-Day Forecast

**App Name:** MyObservatory (iPhone)
**Feature:** 9-Day Forecast
**Path:** Side Panel -> Forecast & Warning Services -> 9-Day Forecast

## Pre-conditions
1.  "MyObservatory" app is installed on an iPhone.
2.  Device has an active internet connection (Wi-Fi or Cellular).
3.  App is launched and on the home screen.

## 1. Navigation

| ID | Test Case Description | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **NAV-001** | Verify navigation to "9-Day Forecast" page | 1. Tap the "Menu" icon (Side Panel) at the top left.<br>2. Tap "Forecast & Warning Services".<br>3. Tap "9-Day Forecast". | The "9-Day Forecast" page opens successfully. The title bar displays "9-Day Forecast". |
| **NAV-002** | Verify "Back" navigation | 1. Navigate to the "9-Day Forecast" page.<br>2. Tap the "Back" button (or arrow) in the top left corner. | User is returned to the "Forecast & Warning Services" menu or previous screen. |

## 2. UI Verification

| ID | Test Case Description | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **UI-001** | Verify Page Title | 1. Navigate to the "9-Day Forecast" page. | The title "9-Day Forecast" is clearly visible at the top. |
| **UI-002** | Verify General Situation Text | 1. Observe the text section below the title. | A paragraph describing the "General Situation" is displayed. Text is readable and aligned correctly. |
| **UI-003** | Verify Forecast List Display | 1. Observe the list of forecast days. | A list containing 9 distinct entries (one for each of the next 9 days) is displayed. |
| **UI-004** | Verify Individual Day Elements | 1. Inspect a single day's row in the list. | Each row should display:<br>- Date (e.g., 21 Jan)<br>- Day of the week (e.g., Wed)<br>- Weather Icon<br>- Temperature Range (Low - High, e.g., 15 - 19°C)<br>- Humidity Range (e.g., 70 - 95%)<br>- Short weather description (e.g., Cloudy with rain). |
| **UI-005** | Verify Probability of Significant Rain (PSR) | 1. Check if PSR information is displayed (if applicable/enabled in settings). | PSR probability (e.g., "Low", "Medium", "High") is displayed if the feature is supported and active. |
| **UI-006** | Verify Layout on different screen sizes | 1. Test on iPhone SE (small screen) and iPhone Pro Max (large screen). | Content scales appropriately. No text overlap or truncation. |
| **UI-007** | Verify Dark Mode Support | 1. Enable system-wide Dark Mode on iPhone.<br>2. Open the page. | Background becomes dark, text becomes light. Contrast is sufficient and readable. |

## 3. Functionality

| ID | Test Case Description | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **FUNC-001** | Verify Data Freshness | 1. Open the page.<br>2. Compare data with the official HKO website. | The forecast data (temps, humidity, text) matches the official HKO data. |
| **FUNC-002** | Verify Pull-to-Refresh | 1. On the "9-Day Forecast" page, pull down the list and release. | A loading indicator appears. The data refreshes (timestamp may update if visible). |
| **FUNC-003** | Verify Scrolling | 1. Scroll down to the bottom of the 9-day list.<br>2. Scroll back up. | Scrolling is smooth. The 9th day is fully visible at the bottom. |
| **FUNC-004** | Verify Language Switching (English <-> Traditional Chinese) | 1. Go to App Settings -> Language -> Select "Traditional Chinese".<br>2. Navigate to "9-Day Forecast". | Page title changes to "九天天氣預報". All content (General Situation, Days, Weather terms) is in Traditional Chinese. |
| **FUNC-005** | Verify Share Functionality (if available) | 1. Look for a "Share" button (usually top right).<br>2. Tap it. | The iOS share sheet opens, allowing sharing of the forecast text/image to other apps. |

## 4. Edge Cases

| ID | Test Case Description | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **EDGE-001** | Verify behavior with No Internet Connection | 1. Turn on Airplane Mode.<br>2. Navigate to "9-Day Forecast" (or pull to refresh if already there). | An error message (e.g., "Network Error" or "Please check your connection") is displayed. Cached data might be shown with a warning. |
| **EDGE-002** | Verify App Background/Foreground | 1. Open "9-Day Forecast".<br>2. Minimize the app (Home screen).<br>3. Wait 5 minutes.<br>4. Re-open the app. | The app resumes on the "9-Day Forecast" page. Data might auto-refresh depending on app logic. |
| **EDGE-003** | Verify Orientation Change (if supported) | 1. Rotate device to Landscape mode. | **If supported:** Layout adjusts to landscape.<br>**If locked:** Screen remains in portrait mode (most utility apps lock to portrait). |
