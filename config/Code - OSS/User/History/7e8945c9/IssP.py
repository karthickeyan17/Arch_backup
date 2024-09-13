import requests
import json
from datetime import datetime, timezone

# Define the GraphQL query to retrieve user problem solved data
query = '''
query userCalendar($username: String!) {
  matchedUser(username: $username) {
    userCalendar {
      submissionCalendar
    }
  }
}
'''

# Define the variables
variables = {
    "username": "ashokkumarr2004"  # Replace with the desired username
}

# Send the POST request to the GraphQL endpoint
response = requests.post(
    "https://leetcode.com/graphql/",
    json={"query": query, "variables": variables}
)

# Parse the response as JSON
data = response.json()

# Function to convert Unix timestamp to date
def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(int(timestamp), timezone.utc).strftime('%Y-%m-%d')

# Function to list problems solved within a date range
def list_problems_solved(start_date, end_date):
    if 'data' in data and 'matchedUser' in data['data']:
        calendar_data = data['data']['matchedUser']['userCalendar']['submissionCalendar']
        submission_calendar = json.loads(calendar_data)
        
        start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
        end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())

        problems_solved = []
        for timestamp, count in submission_calendar.items():
            date = timestamp_to_date(timestamp)
            if start_date <= date <= end_date:
                problems_solved.append({
                    'date': date,
                    'count': count
                })

        return problems_solved
    else:
        print("Error: No data found in response.")
        print("Response data:", data)  # Debugging line
        return []

# Define your date range
start_date = '2024-02-01'  # Start date in 'YYYY-MM-DD' format
end_date = '2024-08-31'    # End date in 'YYYY-MM-DD' format

# List the problems solved within the date range
problems_solved = list_problems_solved(start_date, end_date)

# Print the result
print(f"Problems solved between {start_date} and {end_date}:")
for entry in problems_solved:
    print(f"Date: {entry['date']}, Number of problems solved: {entry['count']}")
