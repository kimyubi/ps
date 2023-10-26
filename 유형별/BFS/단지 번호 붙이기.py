from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

queue = deque()
result = list()

def bfs(x,y):
    cnt = 1
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
for x in sorted(result):
    print(x)