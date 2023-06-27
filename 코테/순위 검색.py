from itertools import combinations
from bisect import bisect_left
from collections import defaultdict

def make_case(info, infoDict):
    tempArr = info.split(" ")
    score = int(tempArr[-1])
    
    for idx in range(5):
        for c in combinations(tempArr[:-1], idx):
            key = "".join(c)
            infoDict[key].append(score)
            

# 이진탐색으로 queryScore 보다 큰 점수들의 개수 반환
def find_answer(key, queryScore, infoDict):
    if key in infoDict:
        return len(infoDict[key]) - bisect_left(infoDict[key], queryScore)
    return 0

def solution(informations, query):
    infoDict = defaultdict(list)
    
    for info in informations:
        make_case(info, infoDict)
    
    for key in infoDict.keys():
        infoDict[key].sort()
        
    answer = []
    for x in query:
        tempArr = list(y for y in x.replace("and", " ").replace("-", "").split(" "))
        queryScore = int(tempArr[-1])
        
        if len(tempArr) == 1:
            answer.append(find_answer("", queryScore, infoDict))
        else:
            answer.append(find_answer("".join(tempArr[:-1]), queryScore, infoDict))
            
    return answer