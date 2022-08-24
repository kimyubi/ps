from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph):
    queue = deque([(0,0)])
    r,c = len(graph), len(graph[0])
    visited = [[0] * c for _ in range(r)]
    
    
    visited[0][0] = True
    
    while queue:
        x,y = queue.popleft()
        if x == r-1 and y == c-1:
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                
    return -1
        
    
    
def solution(maps):
    answer = bfs(maps)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))