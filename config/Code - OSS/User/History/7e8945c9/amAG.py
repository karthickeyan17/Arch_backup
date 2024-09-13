import requests
import json
from datetime import datetime

# Define the GraphQL query to retrieve user problem solved data
query = '''
query userCalendar($username: String!) {
  matchedUser(username: $username) {
    userCalendar {
      submissionCalendar
      solvedProblems {
        problemId
        date
      }
    }
  }
}
'''

# Define the variables
variables = {
    "username": "karthickeyan_s"  # Replace with the desired username
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
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

# Function to count problems solved within a date range and list the problem IDs
def count_problems_solved(start_date, end_date):
    if 'data' in data and 'matchedUser' in data['data']:
        calendar_data = data['data']['matchedUser']['userCalendar']['submissionCalendar']
        solved_problems_data = data['data']['matchedUser']['userCalendar']['solvedProblems']
        
        submission_calendar = json.loads(calendar_data)
        
        start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
        end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())

        total_solved = 0
        problem_ids = []

        for timestamp, count in submission_calendar.items():
            date = timestamp_to_date(timestamp)
            if start_date <= date <= end_date:
                total_solved += count
                for problem in solved_problems_data:
                    problem_date = timestamp_to_date(problem['date'])
                    if start_date <= problem_date <= end_date:
                        problem_ids.append(problem['problemId'])

        return total_solved, list(set(problem_ids))  # Remove duplicates
    else:
        return 0, []

# Define your date range
start_date = '2024-08-01'  # Start date in 'YYYY-MM-DD' format
end_date = '2024-08-31'    # End date in 'YYYY-MM-DD' format

# Count the number of problems solved within the date range and get problem numbers
problems_solved, problem_numbers = count_problems_solved(start_date, end_date)

# Print the result
print(f"Number of problems solved between {start_date} and {end_date}: {problems_solved}")
print(f"Problem numbers solved: {', '.join(problem_numbers)}")
