# dist 고르는게 잘못됐다..! 낼 다시 풀기
from collections import deque
def solution(n, weak, dist):
    friend_num = len(dist)
    dist.sort()
    dist = deque(dist)
    
    weak = [-1 * (n - x) if n/2 < x else x for x in weak]
    weak.sort()
    weak = deque(weak)
    
    while dist:
        if not weak:
            return friend_num - len(dist)
        
        friend = dist.pop()
        start, end = weak.popleft(), 0
        
        for idx, value in enumerate(weak):
            if friend < value - start:
                break
            end += 1
            
        for _ in range(end):
            weak.popleft()
        
    return -1