from datetime import datetime
import requests
import json
import cache as cacheManager
import time

def getUsername(link):
    link = link.replace("https:","").replace("leetcode.com","").replace("u/","")
    return link.replace("/","")

def getDifficulty(problemTitle):

    # Check difficulty in cache
    cacheManager.initIfNot()
    if(cacheManager.checkCache(problemTitle)):
        return cacheManager.getCache(problemTitle)

    body = """query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
  }
}"""

    variables = {"titleSlug":problemTitle}

    try:
        response = json.loads(requests.get("https://leetcode.com/graphql/",json={"query": body,"variables":variables}).content)
        response = response['data']['question']['difficulty']
        cacheManager.addCache(problemTitle,response)
    except:
        response = "Null"
    finally:
        return response


def getProblems(link):
    username = getUsername(link)

    print("Fetching for username:",username)

    body = '''query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    titleSlug
    timestamp
  }
}'''
    variables = {"username": username,"limit":20}

    response = requests.get("https://leetcode.com/graphql/",json={"query": body,"variables":variables}).content
    try:
        response = json.loads(response)
    except:
        print("Unable to scrape profile")
        print("Response from server:",response.decode('UTF-8'))
        return {}

    submissionList = response['data']['recentAcSubmissionList']
    submissionByDate = {}    

    for submission in submissionList:
        dt = datetime.fromtimestamp(int(submission['timestamp']))
        
        submission['difficulty'] = getDifficulty(submission['titleSlug'])

        if(dt.date() not in submissionByDate.keys()):
            submissionByDate[dt.date()] = {"Easy":0,"Medium":0,"Hard":0}
        submissionByDate[dt.date()][submission['difficulty'].replace("\n","")]+=1

    return submissionByDate

def print_problems_solved(link):
    problems=getProblems(link)
    for date in problems:
        print(date)
        for problem in problems[date]:
            print(problem["title"],problem['difficulty'])
        print("\n")

if __name__ == "__main__":
    getProblems("https://leetcode.com/u/ve/")

