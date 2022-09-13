from collections import Counter
import sys
MAX = sys.maxsize
cnt, result = 0, MAX

s = []
def dfs(begin,target,words):
    global s, result, cnt

    if s and s[-1] == target:        
        result = min(result, len(s))
        return
    else:
        cnt += 1        
    
    for word in words:        
        if word not in s and len(Counter(begin) - Counter(word)) == 1:
            s.append(word)
            dfs(word, target, words)
            s.pop()
    
    
    return result
    
        
    
    
# begin을 target으로 변환하는 최소 단계
def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = dfs(begin,target,words)
    if (answer == MAX):
        return 0
    else:
        return answer
        