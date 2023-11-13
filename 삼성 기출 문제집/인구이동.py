import sys
from collections import deque
input = sys.stdin.readline

# 땅의 크기 N, 
# 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global visited
    queue = deque()
    queue.append([x, y])
    
    visited[x][y] = True
    result = []
    
    while queue:
        x, y = queue.popleft()
        result.append([x, y])
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and L <= abs(A[x][y] - A[nx][ny]) <= R:
                    queue.append([nx, ny]) 
                    visited[nx][ny] = True
    
    return result
    
answer = 0
while True:
    visited = [[False] * N for _ in range(N)]
    is_moveable = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = bfs(i, j)
                len_union = len(union)
                if 1 < len_union:
                    sum = 0
                    for city_x, city_y in union:
                        sum += A[city_x][city_y]
                    
                    sum //= len_union
                    for city_x, city_y in union:
                        A[city_x][city_y] = sum
                        
                    is_moveable = True
                    
    if not is_moveable:
        break
    answer += 1
    
print(answer)
                        
                    
                
                
            
