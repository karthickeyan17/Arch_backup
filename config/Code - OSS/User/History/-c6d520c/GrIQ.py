import requests
import json
from datetime import datetime, timezone

# Define the GraphQL query to retrieve progress list data
query = '''
query progressList($pageNo: Int, $numPerPage: Int, $filters: ProgressListFilterInput) {
  isProgressCalculated
  solvedQuestionsInfo(pageNo: $pageNo, numPerPage: $numPerPage, filters: $filters) {
    currentPage
    pageNum
    totalNum
    data {
      totalSolves
      question {
        questionFrontendId
        questionTitle
        questionDetailUrl
        difficulty
        topicTags {
          name
          slug
        }
      }
      lastAcSession {
        time
        wrongAttempts
      }
    }
  }
}
'''

# Define the variables for pagination and filters
variables = {
    "pageNo": 1,
    "numPerPage": 10,
    "filters": {
        "orderBy": "FRONTEND_ID",
        "sortOrder": "ASCENDING"
    }
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
    if 'data' in data and 'solvedQuestionsInfo' in data['data']:
        problems_solved = []
        for item in data['data']['solvedQuestionsInfo']['data']:
            question = item['question']
            last_ac_session = item['lastAcSession']
            last_ac_time = datetime.fromtimestamp(last_ac_session['time'], timezone.utc).strftime('%Y-%m-%d')
            
            if start_date <= last_ac_time <= end_date:
                problems_solved.append({
                    'date': last_ac_time,
                    'question_id': question['questionFrontendId'],
                    'title': question['questionTitle'],
                    'difficulty': question['difficulty'],
                    'total_solves': item['totalSolves'],
                    'url': question['questionDetailUrl']
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
    print(f"Date: {entry['date']}, Problem ID: {entry['question_id']}, Title: {entry['title']}, Difficulty: {entry['difficulty']}, Total Solves: {entry['total_solves']}, URL: {entry['url']}")
