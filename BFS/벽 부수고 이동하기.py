# n개의 줄, m개의 숫자
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# visited[x][y][w]가 0이면 벽을 뚫지 않은 경우, 1이면 벽을 뚫은 경우
def bfs():    
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    
    while queue:
        x,y,w = queue.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][w]
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 경로에 벽이 없는 경우
                if graph[nx][ny] == 0 and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx,ny,w))
                    
                # 경로에 벽이 있고, 아직 벽을 부수지 않은 경우
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    queue.append((nx,ny,w+1))
                    
    return -1
                     

print(bfs())