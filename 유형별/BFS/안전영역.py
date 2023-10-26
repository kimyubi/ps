from collections import deque
from re import L
import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

def bfs(x,y,visited,v):
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > v and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

def solution(x):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > x and not visited[i][j]:
                bfs(i,j,visited,x)
                cnt += 1
    return cnt
    
result = []

# 높이는 1이상 100 이하의 정수
for v in range(0,100+1):
    result.append(solution(v))
    
print(max(result))
    

