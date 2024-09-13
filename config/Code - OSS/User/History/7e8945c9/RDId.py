import requests
import json
from datetime import datetime

# Define the GraphQL query to retrieve user problem solved data
calendar_query = '''
query userCalendar($username: String!) {
  matchedUser(username: $username) {
    userCalendar {
      submissionCalendar
    }
  }
}
'''

# Define the GraphQL query to retrieve problem details
problems_query = '''
query allQuestionsBeta($limit: Int!) {
  allQuestionsBeta(limit: $limit, offset: 0) {
    questionId
    title
    titleSlug
    difficulty
  }
}
'''

# Define the variables
calendar_variables = {
    "username": "karthickeyan_s"  # Replace with the desired username
}

problems_variables = {
    "limit": 1000  # Adjust the limit as needed
}

# Function to convert Unix timestamp to date
def timestamp_to_date(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

# Function to count problems solved within a date range with difficulty
def count_problems_by_difficulty(start_date, end_date):
    # Fetch user calendar data
    calendar_response = requests.post(
        "https://leetcode.com/graphql/",
        json={"query": calendar_query, "variables": calendar_variables}
    )
    calendar_data = calendar_response.json()

    if 'data' in calendar_data and 'matchedUser' in calendar_data['data']:
        calendar_data = calendar_data['data']['matchedUser']['userCalendar']['submissionCalendar']
        submission_calendar = json.loads(calendar_data)
        
        start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
        end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())

        # Fetch problem details data
        problems_response = requests.post(
            "https://leetcode.com/graphql/",
            json={"query": problems_query, "variables": problems_variables}
        )
        problems_data = problems_response.json()

        problems = {}
        if 'data' in problems_data and 'allQuestionsBeta' in problems_data['data']:
            for problem in problems_data['data']['allQuestionsBeta']:
                problems[problem['titleSlug']] = problem['difficulty']

        # Count problems by difficulty
        difficulty_count = {'easy': 0, 'medium': 0, 'hard': 0}
        for timestamp, count in submission_calendar.items():
            date = timestamp_to_date(timestamp)
            if start_date <= date <= end_date:
                for _ in range(count):
                    problem_slug = list(problems.keys())[0]  # Replace with actual problem slug
                    difficulty = problems.get(problem_slug, 'unknown')
                    if difficulty in difficulty_count:
                        difficulty_count[difficulty] += 1

        return difficulty_count
    else:
        return {'easy': 0, 'medium': 0, 'hard': 0}

# Define your date range
start_date = '2024-08-01'  # Start date in 'YYYY-MM-DD' format
end_date = '2024-08-31'    # End date in 'YYYY-MM-DD' format

# Count the number of problems solved by difficulty within the date range
difficulty_counts = count_problems_by_difficulty(start_date, end_date)

# Print the result
print(f"Number of problems solved between {start_date} and {end_date} by difficulty:")
print(f"Easy: {difficulty_counts['easy']}")
print(f"Medium: {difficulty_counts['medium']}")
print(f"Hard: {difficulty_counts['hard']}")
