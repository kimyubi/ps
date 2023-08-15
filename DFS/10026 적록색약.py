import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
painting = [list(input().rstrip()) for _ in range(n)]

def bfs(x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    signatue = painting[x][y]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and painting[nx][ny] == signatue:
                    visited[nx][ny] = True
                    queue.append([nx, ny])    
                    
def normal():  
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1    
    return cnt

def red_green():  
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if painting[i][j] == 'G':
                painting[i][j] = 'R'
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1    
    return cnt

print(normal(), red_green())
