import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global visited
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
        

for _ in range(int(input())):
    # 배추 밭의 가로 길이 m, 세로 길이 n, y배추가 심어져 있는 위치의 개수 k
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
                
    print(cnt)
            