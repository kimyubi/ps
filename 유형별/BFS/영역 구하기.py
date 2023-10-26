from collections import deque
from re import L
import sys

input = sys.stdin.readline
M,N,K = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    graph[x][y] = 1
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and not graph[nx][ny]:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                cnt += 1
                
    return cnt
    
    
graph = [[0] * N for _ in range(M)] 
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for s in range(y1, y2):
        for k in range(x1, x2):
            graph[s][k] = 1
                
result = []
for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                result.append(bfs(i,j))
    
print(len(result))
print(*sorted(result))

            
    