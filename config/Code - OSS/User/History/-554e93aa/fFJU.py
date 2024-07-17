cache = {}
CACHE_PATH = "./cache.txt"

def initIfNot():
    if(len(cache)!=0):
        return
    f = open(CACHE_PATH,"r")
    for line in f.readlines():
        p,d = line.split(",")
        cache[p] = d
    f.close()
def addCache(problem,difficulty):
    f = open(CACHE_PATH,"a")
    f.write(problem+","+difficulty+"\n")
    f.close()
    cache[problem] = difficulty
    print("added cache:",problem,difficulty)

def getCache(problem):
    return cache[problem]

def checkCache(problem):
    return problem in cache.keys()