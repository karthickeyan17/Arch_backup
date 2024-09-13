import requests

"""query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
  }
}"""
# Define the GraphQL query
query = """
{
  user(username: "karthickeyan_s") {
    username
    profile {
      realName
      aboutMe
    }
    submissionCalendar
  }
}
"""

# Send the POST request to the GraphQL endpoint
response = requests.post(
    "https://leetcode.com/graphql/",
    json={"query": query}
)

# Print the response
print(response.json())
