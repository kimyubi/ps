import sys
from collections import deque

input = sys.stdin.readline
low, high = 1, 1000000000

# n개의 섬
n, m = map(int, input().split())
bridge = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, weight_limit = map(int, input().split())
    bridge[a].append([b,weight_limit])
    bridge[b].append([a,weight_limit])
    
f1, f2 = map(int, input().split())

def bfs(mid):
    visited = [False for _ in range(n + 1)]
    visited[f1] = True
    queue = deque([f1])

    while queue:
        now = queue.popleft()
        if now == f2:
            return True
        
        for next, weight_limit in bridge[now]:
            if not visited[next] and mid <= weight_limit:
                queue.append(next)
                visited[next] = True
    return False

while low <= high:
        mid = (low + high) // 2
        if bfs(mid):
            low = mid + 1
        else: 
            high = mid - 1
            
print(high)