import requests

def fetch_recent_submissions(username, limit=50):
    # Define the GraphQL query without pagination to check the initial response
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
        "username": username,
        "limit": limit  # Request up to 50 submissions
    }

    # Send the POST request to the GraphQL endpoint
    response = requests.post(
        "https://leetcode.com/graphql/",
        json={"query": query, "variables": variables}
    )

    # Parse the response as JSON
    data = response.json()

    # Print the entire response to debug
    print("Response Data:")
    print(data)

    # Check if there are submissions in the response
    if 'data' in data and 'recentAcSubmissionList' in data['data']:
        submissions = data['data']['recentAcSubmissionList']
        return submissions
    else:
        return []

# Example usage
username = "karthickeyan_s"  # Replace with the desired username
limit = 50
submissions = fetch_recent_submissions(username, limit)

# Print the number of submissions retrieved
print(f"Number of submissions retrieved: {len(submissions)}")

# Optionally, print all submissions
for submission in submissions:
    print(submission)
