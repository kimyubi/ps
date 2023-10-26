import sys
from collections import deque

input = sys.stdin.readline

hx = [1,1,2,2,-1,-1,-2,-2]
hy = [-2,2,-1,1,-2,2,-1,1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

K = int(input())
W,H = map(int, input().split())

# 말을 움직인 횟수에 따른 각각의 이동 경로를 visited에 기록한다. (0 ~ K)번이므로 K+1개의 공간을 만들어준다.
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
graph = [list(map(int,input().rstrip().split())) for _ in range(H)]

def bfs():
    queue = deque([(0,0,K)])
    
    while queue:
        x,y,k = queue.popleft()
        
        if x == H-1 and y == W-1:
            return visited[x][y][k]
        
        
        # 말처럼 움직일 수 있다면
        if k > 0:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                
                if 0 <= nx < H and 0 <= ny < W:
                    if graph[nx][ny] == 0 and not visited[nx][ny][k-1]:
                        visited[nx][ny][k-1] = visited[x][y][k] + 1
                        queue.append((nx,ny,k-1))
                        
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx,ny,k))
                    
        
    return -1
    

print(bfs())
                    
            
        