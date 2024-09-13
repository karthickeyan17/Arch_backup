import requests

def fetch_recent_submissions(username, limit=50):
    submissions = []
    end_cursor = None
    
    while len(submissions) < limit:
        # Define the GraphQL query with pagination
        query = '''
        query recentAcSubmissions($username: String!, $limit: Int!, $cursor: String) {
          recentAcSubmissionList(username: $username, limit: $limit, cursor: $cursor) {
            titleSlug
            timestamp
          }
        }
        '''

        # Define the variables
        variables = {
            "username": username,
            "limit": min(limit - len(submissions), 20),  # Fetch up to 20 per request or the remaining needed
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

            # If the number of submissions returned is less than the requested limit, we're likely done
            if len(current_submissions) < variables['limit']:
                break

            # Assume the API might return a cursor for the next page; if it doesn't, you'd need to modify this logic
            # Here we're just simulating as if `cursor` would be a returned field
            end_cursor = current_submissions[-1]['timestamp']  # You may need to adjust this to the actual cursor if provided

        else:
            # No more data or an error occurred
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
