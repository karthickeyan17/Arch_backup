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

# Wait until the user logs in
logged_in = False

while not logged_in:
    try:
        # Check for an element that appears only after login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http/']"))
        )
        logged_in = True
    except:
        print("User is not logged in yet. Waiting...")

# Navigate to the progress page once logged in
driver.get(progress_url)

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
