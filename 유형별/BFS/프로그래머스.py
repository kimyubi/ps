from collections import deque
def bfs(x, y, visited, table, n):
    queue = deque([x,y])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end = '')
        
        
         