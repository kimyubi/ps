from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1 ,1, -1, 1, 1, -1]
    
    graph = [[0] * 51 for _ in range(51)]
    
    
    for min_c, min_r, max_c, max_r in rectangle:
        for i in range(min_r, max_r + 1):
            for j in range(min_c, max_c+1):
                if not graph[i][j]:
                    graph[i][j] = 1
    
    graph[characterY][characterX] = 2
    graph[itemY][itemX] = 3
    
    graph = graph[::-1]
    
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    for i in range(51):
        for j in range(51):
            if graph[i][j] != 0:
                if graph[i][j] == 2:
                    start_x, start_y = i, j
                if graph[i][j] == 3:
                    end_x, end_y = i, j
                
                
                is_border = False
                for x in range(8):
                    nx, ny = i + dx[x], j + dy[x]
                    if graph[nx][ny] == 0:
                        is_border = True
                        break
                
                if not is_border:
                    graph[i][j] = 9
                                        
    
    visited = [[0] * 51 for _ in range(51)]
    
    queue = deque()
    queue.append([start_x, start_y])
    
    visited[start_x][start_y] = 1
    
    #for g in graph:
    #    print(''.join(list(map(str, g))))
        
    while queue:
        x, y = queue.popleft()
        
        if x == end_x and y == end_y:
            return visited[x][y] -1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 51 and 0 <= ny < 51:
                if graph[nx][ny] in (1,3) and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                
    
        
    
        