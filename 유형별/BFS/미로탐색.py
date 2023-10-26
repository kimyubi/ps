import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    result = 10 ** 6
    queue = deque([(x,y,1)])
    visited[x][y] = True

    while queue:
        x, y, d = queue.popleft()
        
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':   
                 
                if nx == n-1 and ny == m-1 :
                    result = min(result,d+1)
                    
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,d+1))
                    print(queue) 

    return result
                     
print(bfs(0,0))
