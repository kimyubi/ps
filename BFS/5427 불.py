from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    w, h = map(int,input().split())
    
    graph = [list(input().strip()) for _ in range(h)]
    f_queue, s_queue = deque(), deque()
    f_visited, s_visited = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                f_queue.append((i,j))
                f_visited[i][j] = 1
            
            elif graph[i][j] == '@':
                s_queue.append((i,j))
                s_visited[i][j] = 1
    
    
    while f_queue:
        x,y = f_queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w :
                if graph[nx][ny] != '#' and not f_visited[nx][ny]:
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny))
    while s_queue:
        x,y = s_queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != '#' and not s_visited[nx][ny]:
                    if not f_visited[nx][ny] or f_visited[nx][ny] > s_visited[x][y] + 1:
                        s_visited[nx][ny] = s_visited[x][y] + 1
                        s_queue.append((nx,ny))
            
            else:
                return s_visited[x][y]
            
    return "IMPOSSIBLE"            


for _ in range(n):
    print(bfs())
    
    
