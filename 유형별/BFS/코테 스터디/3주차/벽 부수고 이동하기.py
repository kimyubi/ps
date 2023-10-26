from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# 0은 이동할 수 있는 곳, 1은 이동할 수 없는 벽이 있는 곳
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[[0, 0] for j in range(m)] for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# visited[x][y][0] 은 벽을 부수지 않은 경우의 최단거리
# visited[x][y][1] 은 벽을 부순 경우의 최단거리

def solution():
    
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    
    while queue:
        x, y, k = queue.popleft() 
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][k]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                 # 경로에 벽이 없는 경우
                if graph[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx,ny,k))
                    
                # 경로에 벽이 있고, 아직 벽을 부수지 않은 경우
                elif graph[nx][ny] == 1 and k == 0:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    queue.append((nx,ny,k+1))
    
                
    return -1


print(solution())               
        
            
            
    