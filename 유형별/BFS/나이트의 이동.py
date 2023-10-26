import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [-2,2,-1,1,-2,2,-1,1]

def bfs():
    l = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    
    queue = deque([(now_x,now_y)])
    visited = [[0] * l for _ in range(l)]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if x == goal_x and y == goal_y:
                return(visited[x][y])
                
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

for i in range(n):
    print(bfs())
    
            
         