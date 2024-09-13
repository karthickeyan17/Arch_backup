import requests

payload = {
    'id_login': 'scraper12',
    'id_password': '9994366529k'
}
url='https://leetcode.com/accounts/login/?next='
# Create a session object
with requests.Session() as s:
    # Perform the POST request to login
    response = s.post(url, data=payload)

    # Check if login was successful
    if response.ok:
        print("Login successful")
        # Optionally, print or process the response
        print(response.text)
    else:
        print(f"Login failed with status code {response.status_code}")
