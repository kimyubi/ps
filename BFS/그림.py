import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
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
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    width += 1
                    queue.append((nx,ny))
    return width
    
cnt, width = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt +=1 
            width = max(width, bfs(i,j))
            
print(cnt)
print(width)
             