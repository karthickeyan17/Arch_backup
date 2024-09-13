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
username = "karthickeyan_s"
progress_info = fetch_leetcode_user_progress(username)
print(progress_info.dict())
