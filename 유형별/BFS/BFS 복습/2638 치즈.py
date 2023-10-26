import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

n, m = map(int, input().split())
# 치즈가 있는 부분 1, 치즈가 없는 부분 0
map = [list(map(int, input().split())) for _ in range(n)]

def melted():
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    
    # 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다
    queue.append([0,0])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 외부 공기
                if not map[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    
                # 치즈
                else:
                    visited[nx][ny] += 1
    
    sum = 0                
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                map[i][j] = 0
            
            sum += map[i][j]
    return sum
                
                
ans = 0    
while True:
    result = melted()
    ans += 1
    
    if not result:
        break
    
print(ans)
    
    