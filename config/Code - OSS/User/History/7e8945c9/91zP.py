import requests

def fetch_recent_submissions(username, target_limit=50):
    submissions = []
    end_cursor = None

    while len(submissions) < target_limit:
        # Define the GraphQL query with pagination
        query = '''
        query recentAcSubmissions($username: String!, $limit: Int!, $cursor: String) {
          recentAcSubmissionList(username: $username, limit: $limit, lastKey: $cursor) {
            titleSlug
            timestamp
          }
        }
        '''

        # Define the variables
        variables = {
            "username": username,
            "limit": min(20, target_limit - len(submissions)),  # LeetCode might return up to 20 per page
            "cursor": end_cursor
        }

        # Send the POST request to the GraphQL endpoint
        response = requests.post(
            "https://leetcode.com/graphql/",
            json={"query": query, "variables": variables}
        )

        # Parse the response as JSON
        data = response.json()

        # Check if there are submissions in the response
        if 'data' in data and 'recentAcSubmissionList' in data['data']:
            current_submissions = data['data']['recentAcSubmissionList']
            submissions.extend(current_submissions)

            # Break if fewer submissions are returned than requested, meaning we've fetched all available submissions
            if len(current_submissions) < variables['limit']:
                break

            # Update end_cursor to the timestamp of the last submission
            end_cursor = current_submissions[-1]['timestamp']
        else:
            # If no data or an error occurred, exit the loop
            break

    return submissions

# Example usage
username = "karthickeyan_s"  # Replace with the desired username
limit = 50
all_submissions = fetch_recent_submissions(username, limit)

# Print the number of submissions retrieved
print(f"Number of submissions retrieved: {len(all_submissions)}")

# Optionally, print all submissions
for submission in all_submissions:
    print(submission)
