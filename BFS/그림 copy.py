import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    width = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+ dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny <m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    
cnt, width = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i,j)
            cnt +=1 
            
print(cnt)
             