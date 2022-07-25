from collections import deque
import sys

input = sys.stdin.readline
m,n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

point = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            point.append((i,j))
            
if len(point) == 0:
    print(-1)
elif len(point) == n*m:
    print(0)
else:
    while point:
        x, y = point.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0 and graph[x][y] != -1:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] == True
                    point.append((nx,ny))

    if any(0 in l for l in graph): 
        print(-1)
    else:
        print(max(map(max, graph))-1)