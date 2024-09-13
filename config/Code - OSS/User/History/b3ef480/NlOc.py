from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (e.g., Firefox)
driver = webdriver.Firefox()

# Navigate to the login page
driver.get('https://leetcode.com/accounts/login/')

# Enter username and password
username = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')
username.send_keys('your_username')
password.send_keys('your_password')

# Submit the login form
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
login_button.click()

# Wait for login to complete and redirection to occur
WebDriverWait(driver, 10).until(EC.url_to_be('https://leetcode.com/'))

# Navigate to the progress page
driver.get('https://leetcode.com/progress/')

# Optionally, scrape or process the page
print(driver.page_source)

# Close the browser session
driver.quit()
