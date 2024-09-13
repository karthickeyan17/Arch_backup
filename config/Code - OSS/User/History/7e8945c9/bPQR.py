import requests

# Define the GraphQL query
query = """
{
  userProfilePublicProfile(userSlug: "your_username") {
    username
    realName
    aboutMe
    school
    skillTags
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
