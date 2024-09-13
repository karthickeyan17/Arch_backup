import requests

# Define the GraphQL query
query = '''
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    titleSlug
    timestamp
  }
}
'''

# Define the variables
variables = {
    "username": "karthickeyan_s",  # Replace with the desired username
    "limit": 50  # Adjust the limit as needed
}

# Send the POST request to the GraphQL endpoint
response = requests.post(
    "https://leetcode.com/graphql/",
    json={"query": query, "variables": variables}
)

# Parse the response as JSON (which is already a dictionary)
data = response.json()

# Print the entire response to see what is being returned
print(data)

# Print the number of recent accepted submissions
if 'data' in data and 'recentAcSubmissionList' in data['data']:
    print(f"Number of submissions returned: {len(data['data']['recentAcSubmissionList'])}")
else:
    print("No data found or an error occurred.")
