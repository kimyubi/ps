import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도의 크기 N
N = int(input())
map = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def bfs(i, j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N: 
                if not visited[nx][ny] and map[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    cnt += 1
    return cnt
    


answer = []
for i in range(N):
    for j in range(N):
        if map[i][j]and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(*answer, sep='\n')
