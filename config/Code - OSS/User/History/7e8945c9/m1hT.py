import requests

# Define the GraphQL query to retrieve user profile information
query = '''
query userProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      realName
      aboutMe
      userAvatar
      reputation
      ranking
    }
    submitStats {
      acSubmissionNum {
        count
        difficulty
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

# Print the user's profile information
if 'data' in data and 'matchedUser' in data['data']:
    user_profile = data['data']['matchedUser']
    print("Username:", user_profile['username'])
    print("Real Name:", user_profile['profile']['realName'])
    print("About Me:", user_profile['profile']['aboutMe'])
    print("User Avatar URL:", user_profile['profile']['userAvatar'])
    print("Reputation:", user_profile['profile']['reputation'])
    print("Ranking:", user_profile['profile']['ranking'])

    print("\nSubmission Stats:")
    for stat in user_profile['submitStats']['acSubmissionNum']:
        print(f"Difficulty: {stat['difficulty']}, Count: {stat['count']}")
else:
    print("No data found or an error occurred.")
