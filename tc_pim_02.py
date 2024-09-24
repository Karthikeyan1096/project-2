from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (Assuming ChromeDriver is in your PATH or provide path to ChromeDriver)
driver = webdriver.Chrome()

# Launch the Orange HRM site
url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Precondition: Login as "Admin"
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLogin")

# Enter admin credentials
username.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

# Allow time for the login to complete and the page to load
time.sleep(3)

# Navigate to the Admin page by clicking on the Admin tab
admin_menu = driver.find_element(By.ID, "menu_admin_viewAdminModule")
admin_menu.click()

# Allow time for the Admin page to load
time.sleep(2)

# Step 1: Validate the Title of the Page
expected_title = "OrangeHRM"
actual_title = driver.title

if actual_title == expected_title:
    print(f"Page title validation passed: {actual_title}")
else:
    print(f"Page title validation failed. Expected: {expected_title}, but got: {actual_title}")

# Step 2: Validate that the below options are displayed on Admin Page
expected_options = [
    "User Management", 
    "Job", 
    "Organization", 
    "Qualifications", 
    "Nationalities", 
    "Corporate Banking", 
    "Configuration"
]

# XPaths for the menu options
xpath_options = {
    "User Management": "//a[@id='menu_admin_UserManagement']",
    "Job": "//a[@id='menu_admin_Job']",
    "Organization": "//a[@id='menu_admin_Organization']",
    "Qualifications": "//a[@id='menu_admin_Qualifications']",
    "Nationalities": "//a[@id='menu_admin_nationality']",
    "Corporate Banking": "//a[@id='menu_admin_corporateBanking']",  # Example for Corporate Banking, replace with actual if different
    "Configuration": "//a[@id='menu_admin_Configuration']"
}

# Validate each menu option is visible on the Admin page
for option, xpath in xpath_options.items():
    try:
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed():
            print(f"'{option}' is displayed on the Admin page.")
        else:
            print(f"'{option}' is NOT displayed on the Admin page.")
    except Exception as e:
        print(f"'{option}' is NOT displayed on the Admin page. Exception: {e}")

# Close the browser after validation
driver.quit()
