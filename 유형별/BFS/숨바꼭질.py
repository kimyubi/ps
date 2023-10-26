from collections import deque

MAX = 2000000
visited = [0] * MAX


n,k = map(int, input().split())
queue = deque([n])

while queue:
    x = queue.popleft()
    
    if x == k:
        print(visited[x])
        break
    
    for nx in (x-1, x+1, x*2):
        if 0 <= nx < MAX and not visited[nx]:
            visited[nx] = visited[x] + 1
            queue.append(nx)
        
        
        
    
    
