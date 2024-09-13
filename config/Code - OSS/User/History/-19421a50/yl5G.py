import aiohttp
import asyncio
from datetime import datetime
import json
import cache as cacheManager

def getUsername(link):
    link = link.replace("https:","").replace("leetcode.com","").replace("u/","")
    return link.replace("/","")

async def fetch(session, url, json_body):
    async with session.post(url, json=json_body) as response:
        return await response.text()

async def getDifficulty(session, problemTitle):
    # Check difficulty in cache
    cacheManager.initIfNot()
    if cacheManager.checkCache(problemTitle):
        return cacheManager.getCache(problemTitle)

    body = """query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
  }
}"""
    variables = {"titleSlug": problemTitle}

    try:
        response_text = await fetch(session, "https://leetcode.com/graphql/", {"query": body, "variables": variables})
        response = json.loads(response_text)
        difficulty = response['data']['question']['difficulty']
        cacheManager.addCache(problemTitle, difficulty)
    except Exception as e:
        print(f"Error fetching difficulty for {problemTitle}: {e}")
        difficulty = "Null"

    return difficulty

async def getProblems(link):
    username = getUsername(link)
    print("Fetching for username:", username)

    body = '''query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    titleSlug
    timestamp
  }
}'''
    variables = {"username": username, "limit": 20}

    async with aiohttp.ClientSession() as session:
        response_text = await fetch(session, "https://leetcode.com/graphql/", {"query": body, "variables": variables})
        try:
            response = json.loads(response_text)
        except Exception as e:
            print("Unable to scrape profile")
            print("Response from server:", response_text)
            return {}

        submissionList = response['data']['recentAcSubmissionList']
        submissionByDate = {}

        tasks = []
        for submission in submissionList:
            dt = datetime.fromtimestamp(int(submission['timestamp']))
            task = asyncio.ensure_future(getDifficulty(session, submission['titleSlug']))
            submission['difficulty_task'] = task
            tasks.append(task)

            if dt.date() not in submissionByDate.keys():
                submissionByDate[dt.date()] = {"Easy": 0, "Medium": 0, "Hard": 0}

        difficulties = await asyncio.gather(*tasks)
        for i, submission in enumerate(submissionList):
            difficulty = difficulties[i]
            submissionByDate[datetime.fromtimestamp(int(submission['timestamp'])).date()][difficulty.replace("\n", "")] += 1

        return submissionByDate

def print_problems_solved(problems):
    for date in problems:
        print(date)
        for difficulty, count in problems[date].items():
            print(f"{difficulty}: {count}")
        print("\n")

if __name__ == "__main__":
    link = "https://leetcode.com/u/venkatprabu007/"
    loop = asyncio.get_event_loop()
    problems = loop.run_until_complete(getProblems(link))
    print_problems_solved(problems)
