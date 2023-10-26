import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001 
N,K = map(int, input().split())
path = [0 for _ in range(MAX)]

def solution():
    visited = [0] * MAX
        
    queue = deque([N])
    visited[N] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            print(visited[x] -1)
            
            ans = []
            
            while x != N:
                ans.append(x)
                x = path[x]
                
            ans.append(N)
            ans.reverse()
            print(*ans)
            return
            
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                path[nx] = x
                
                queue.append(nx)
    


    
solution()
        