import sys
from collections import deque

input = sys.stdin.readline


def solution():
    MAX = 200000 
    visited = [0] * MAX
    N,K = map(int, input().split())
    
    queue = deque([N])
    visited[N] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            return visited[x] -1
        
        nx = x * 2
        if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x]
                queue.appendleft(nx)
        
        for nx in (x-1, x+1):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    
    return visited[x] -1    
print(solution())
            
        