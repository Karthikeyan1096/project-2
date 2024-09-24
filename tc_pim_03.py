from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Assuming ChromeDriver is in your PATH or provide path to ChromeDriver)
driver = webdriver.Chrome()

# Launch the Orange HRM site
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximize the browser window
driver.maximize_window()

# Precondition: Login as "Admin"
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLogin")

# Enter admin credentials (you may need to replace these with actual credentials)
username.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

# Allow time for the login to complete and page to load
time.sleep(3)

# Navigate to the Admin page by clicking on the Admin tab
admin_menu = driver.find_element(By.ID, "menu_admin_viewAdminModule")
admin_menu.click()

# Validate the Menu Options on the Side Pane
expected_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]
side_pane_menu = driver.find_elements(By.XPATH, "//div[@id='wrapper']//b")

# Collect text of menu items
menu_text = [item.text for item in side_pane_menu]

# Check if all expected items are present
for expected_item in expected_menu_items:
    if expected_item in menu_text:
        print(f"'{expected_item}' is displayed on the Admin page.")
    else:
        print(f"'{expected_item}' is NOT displayed on the Admin page.")

# Close the browser after validation
driver.quit()
