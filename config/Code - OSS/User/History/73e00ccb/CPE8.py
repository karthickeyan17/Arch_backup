import requests

login_url = 'https://leetcode.com/login'
payload = {
    'username': 'scraper12',
    'password': '9994366529k'
}

session = requests.Session()
response = session.post(login_url, data=payload)
print(response)
# Check if login was successful by inspecting response
