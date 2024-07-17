import requests
import json
import cache as cacheManager
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def getUsername(link):
    link = link.replace("https:", "").replace("leetcode.com", "").replace("u/", "")
    return link.replace("/", "")

def getDifficulty(problemTitles):
    cacheManager.initIfNot()
    difficulties = {}
    for problemTitle in problemTitles:
        if cacheManager.checkCache(problemTitle):
            difficulties[problemTitle] = cacheManager.getCache(problemTitle)
        else:
            difficulties[problemTitle] = "Null"
    body = """query questionTitles($titleSlugs: [String!]!) {
  questions(titleSlugs: $titleSlugs) {
    titleSlug
    difficulty
  }
}"""
    variables = {"titleSlugs": list(difficulties.keys())}
    try:
        response = json.loads(requests.get("https://leetcode.com/graphql/", json={"query": body, "variables": variables}).content)
        for question in response['data']['questions']:
            difficulties[question['titleSlug']] = question['difficulty']
            cacheManager.addCache(question['titleSlug'], question['difficulty'])
    except:
        print("Unable to fetch difficulties")
    finally:
        return difficulties

def getProblems(link):
    username = getUsername(link)
    print("Fetching for username:", username)
    body = '''query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    titleSlug
    timestamp
  }
}'''
    variables = {"username": username, "limit": 20}
    response = requests.get("https://leetcode.com/graphql/", json={"query": body, "variables": variables}).content
    try:
        response = json.loads(response)
    except:
        print("Unable to scrape profile")
        print("Response from server:", response.decode('UTF-8'))
        return {}
    submissionList = response['data']['recentAcSubmissionList']
    submissionByDate = {}
    problemTitles = [submission['titleSlug'] for submission in submissionList]
    difficulties = getDifficulty(problemTitles)
    for submission in submissionList:
        dt = datetime.fromtimestamp(int(submission['timestamp']))
        submission['difficulty'] = difficulties[submission['titleSlug']]
        if dt.date() not in submissionByDate.keys():
            submissionByDate[dt.date()] = {"Easy": 0, "Medium": 0, "Hard": 0}
        submissionByDate[dt.date()][submission['difficulty'].replace("\n", "")] += 1
    return submissionByDate

def fetch_difficulties(problemTitles):
    return getDifficulty(problemTitles)

def main():
    link = "https://leetcode.com/u/venkatprabu007/"
    username = getUsername(link)
    print("Fetching for username:", username)
    body = '''query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    titleSlug
    timestamp
  }
}'''
    variables = {"username": username, "limit": 20}
    response = requests.get("https://leetcode.com/graphql/", json={"query": body, "variables": variables}).content
    try:
        response = json.loads(response)
    except:
        print("Unable to scrape profile")
        print("Response from server:", response.decode('UTF-8'))
        return
    submissionList = response['data']['recentAcSubmissionList']
    problemTitles = [submission['titleSlug'] for submission in submissionList]
    with ThreadPoolExecutor(max_workers=5) as executor:
        difficulties = list(executor.map(fetch_difficulties, [problemTitles[i:i+5] for i in range(0, len(problemTitles), 5)]))
    difficulties = {k: v for d in