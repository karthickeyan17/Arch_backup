import requests

# Define the GraphQL query
query = '''query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $karthickeyan_s, limit: $50) {
    titleSlug
    timestamp
  }
}'''

# Send the POST request to the GraphQL endpoint
response = requests.post(
    "https://leetcode.com/graphql/",
    json={"query": query}
)

# Print the response
print(response.json())
