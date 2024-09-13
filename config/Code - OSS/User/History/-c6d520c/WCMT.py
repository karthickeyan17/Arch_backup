import requests
import json
from datetime import datetime, timezone

# Define the GraphQL query to retrieve progress list data
query = '''
query progressList($username: String!, $pageNo: Int, $numPerPage: Int, $filters: ProgressListFilterInput) {
  user(username: $username) {
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
}
'''

variables = {
    "username": "karthickeyan_s",
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

# Print the response
print(json.dumps(data, indent=2))
