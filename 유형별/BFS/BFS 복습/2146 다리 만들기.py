import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

# 지도의 크기 n
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

# 섬 구분하기
def bfs(i, j, mark):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    island = []
    
    while queue:
        x, y = queue.popleft()
        map[x][y] = mark
        island.append([x,y])
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    return island


visited = [[False] * n for _ in range(n)]
islands = []
mark = 1
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            islands.append(bfs(i, j, mark))
            mark += 1
###

# 섬 간 가장 짧은 다리의 길이 구하기
answer = sys.maxsize
for island in islands:
    queue = deque(island)
    visited = [[-1] * n for _ in range(n)]
    
    mx, my = island[0]
    mark = map[mx][my]
    
    for i, j in island:
        visited[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬에 도착한 경우
                if 0 < map[nx][ny] and map[nx][ny] != mark:
                    answer = min(answer, visited[x][y])
                    break
            
                if map[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
###               
print(answer)