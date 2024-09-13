import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://leetcode.com/accounts/login/'
PROGRESS_URL = 'https://leetcode.com/karthickeyan_s/'

# Initialize a session
session = requests.Session()

# Log in to LeetCode
payload = {
    'login': 'karthickeyan_s',
    'password': '9994366529'
}
session.post(LOGIN_URL, data=payload)

# Scrape progress page
response = session.get(PROGRESS_URL)
soup = BeautifulSoup(response.content, 'lxml')

# Extract relevant data
# For example, retrieving the number of problems solved
solved_problems = soup.find('div', {'class': 'progress__header'}).text
print(solved_problems)
