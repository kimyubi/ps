import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
MAX_HEIGHT = 0
ans = 0

for i in range(n):
    for j in range(n):
        MAX_HEIGHT = max(MAX_HEIGHT, graph[i][j])
        
def bfs(i, j, visited, num):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and num < graph[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    
for num in range(0, MAX_HEIGHT + 2):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if num < graph[i][j] and not visited[i][j]:
                bfs(i, j, visited, num)
                cnt += 1
    ans = max(ans, cnt)
print(ans)            