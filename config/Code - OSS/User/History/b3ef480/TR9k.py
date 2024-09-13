from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Firefox()

# Navigate to the LeetCode page
driver.get('https://leetcode.com/karthickeyan_s/')

# Wait for the page to load, if necessary
driver.implicitly_wait(10)  # seconds

# Extract the data you need
solved_problems = driver.find_element(By.CLASS_NAME, 'progress__header').text
print(solved_problems)

# Close the browser session
driver.quit()
