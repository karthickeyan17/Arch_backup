import requests
payload = {
    'inUserName': 'scraper12',
    'inUserPass': '9994366529k'
}
url='https://leetcode.com/accounts/login/'
# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('LOGIN_URL', data=payload)
    # print the HTML returned or something more intelligent to see if it's a successful login page.
    print(p.text)

    # An authorised request.
    r = s.get('A protected web page URL')
    print(r.text)