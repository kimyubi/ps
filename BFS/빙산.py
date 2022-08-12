from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:
        
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
                    
check = False     
day = 0       
while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    
    result = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)           
                result += 1
                
    
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
        
            if graph[i][j] < 0:
                graph[i][j] = 0
                
    
    if result >= 2:
        check = True
        break
    
    elif result == 0:
        break
    
    day += 1 
    


if check:
    print(day)
    
else:
    print(0)
    
        