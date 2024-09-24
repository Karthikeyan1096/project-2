from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (Assuming ChromeDriver is in your PATH or provide path to ChromeDriver)
driver = webdriver.Chrome()

# Launch the Orange HRM site
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Precondition: Click on the "Forgot Password" link
forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
forgot_password_link.click()

# Wait for the Username textbox to be visible
time.sleep(2)  # Adjust time if needed based on network speed

# Verify that the username textbox is displayed
try:
    username_textbox = driver.find_element(By.NAME, "username")
    if username_textbox.is_displayed():
        print("Username textbox is visible.")
        
        # Provide your username (you may replace this with a valid username)
        username_textbox.send_keys("Admin")
        
        # Click on the "Reset Password" button
        reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        reset_button.click()
        
        # Wait for a response
        time.sleep(3)
        
        # Validate if the success message is displayed (adjust based on actual message)
        success_message = driver.find_element(By.XPATH, "//*[contains(text(),'Reset Password link sent successfully')]")
        if success_message.is_displayed():
            print("Reset Password link sent successfully.")
        else:
            print("Success message not displayed. Test failed.")
    else:
        print("Username textbox is NOT visible. Test failed.")
except Exception as e:
    print(f"Test failed: {e}")

# Close the browser after validation
driver.quit()
