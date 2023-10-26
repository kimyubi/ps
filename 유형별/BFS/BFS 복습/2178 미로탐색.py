import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
maze = [list(map(int,list(input().rstrip()))) for _ in range(n)]

def bfs():
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return visited[x][y] + 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
        

print(bfs())