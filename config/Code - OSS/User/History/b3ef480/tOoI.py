from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (e.g., Firefox)
driver = webdriver.Firefox()

# Define the URL for the LeetCode login and progress page
login_url = 'https://leetcode.com/accounts/login/'
progress_url = 'https://leetcode.com/progress/'

# Navigate to the login page
driver.get(login_url)

# Wait for the login form to appear and interact with it
try:
    # Check if the login form is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_login')))
    
    # Enter username and password
    username = driver.find_element(By.ID, 'id_login')
    password = driver.find_element(By.ID, 'id_password')
    
    username.send_keys('your_username')
    password.send_keys('your_password')
    
    # Click the login button
    login_button = driver.find_element(By.ID, 'signin_btn')
    login_button.click()
    
    # Wait for the page to load after login
    WebDriverWait(driver, 10).until(EC.url_changes(login_url))
    
    # Now navigate to the progress page
    driver.get(progress_url)

except Exception as e:
    print("Login was not successful or the login form was not found.", e)

# After login, retrieve data from the progress page
try:
    # Wait for the progress data to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'progress__header')))

    # Extract and print the progress data
    progress_data = driver.find_element(By.CLASS_NAME, 'progress__header').text
    print("Progress Data:", progress_data)

except Exception as e:
    print("Progress data could not be retrieved.", e)

# Close the browser session
driver.quit()
