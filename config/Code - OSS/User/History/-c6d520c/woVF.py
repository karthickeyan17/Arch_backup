import requests

def fetch_leetcode_user_progress(username, page_no=1, num_per_page=20):
    url = "https://leetcode.com/graphql"
    query = """
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
    """
    variables = {
        "pageNo": page_no,
        "numPerPage": num_per_page,
        "filters": None  # Add any specific filters if needed
    }

    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data.")
        return None

# Example usage
def fetch_leetcode_user_progress_static():
    url = "https://leetcode.com/graphql"
    query = """
    query {
      isProgressCalculated
      solvedQuestionsInfo(pageNo: 1, numPerPage: 20, filters: null) {
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
    """
    response = requests.post(url, json={"query": query})
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"GraphQL Errors: {data['errors']}")
        else:
            return data.get('data', {})
    else:
        print("Failed to retrieve data.")
        return None

# Example usage
progress_info = fetch_leetcode_user_progress_static()
if progress_info:
    print(progress_info)
else:
    print("No progress information found.")

username = "karthickeyan_s"
progress_info = fetch_leetcode_user_progress(username)
print(progress_info)
