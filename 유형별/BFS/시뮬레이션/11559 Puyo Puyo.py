import sys
from collections import deque

input = sys.stdin.readline
graph = [list(input().rstrip()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def bfs(x,y,color,visited):
    global graph
    
    queue = deque([(x,y)])
    puyo_list = [(x,y)]
    
    visited[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and graph[nx][ny] is color:
                    puyo_list.append((nx,ny))
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    
    
    if len(puyo_list) >= 4:
        # 같은 색의 뿌요가 4개 이상 모이면 뿌요를 터뜨린다. 
        for x,y in puyo_list:
            graph[x][y] = '.'
            
        return True
    
    else:
        return False
                    
def move_down():
    global graph
    
    for i in range(6):
        x, position = '.', 11
        for j in range(11,-1,-1):
            if graph[j][i] == '.':
                continue
            
            if x == '.':
                x = graph[j][i]
                
            else:
                graph[position][i] = x
                x = graph[j][i]
                position -= 1
                
            graph[j][i] = '.'
            
        if x != '.':
            graph[position][i] = x  
    
# 터뜨릴 뿌요가 있는지 확인하고, 터뜨리는 함수
def explode():
    global ans 
    
    visited = [[False] * 6 for _ in range(12)]
    chain = False
    
    for i in range(12):
        for j in range(6):
            color = graph[i][j]
            if color !=  '.' and not visited[i][j]:
                is_explode = bfs(i,j,color,visited)
                
                if is_explode:
                    chain = True
    
    # 터뜨릴 뿌요가 존재하여, 터뜨릴 뿌요를 모두 터뜨린 경우   
    # 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어뜨린다.      
    if chain:
        ans += 1
        move_down()
        return True
    
    # 터뜨릴 뿌요가 존재하지 않는 경우
    else:
        return False
        

# 더 이상 터뜨릴 뿌요가 없을 때까지 반복한다.
is_continuity = explode()
while is_continuity:
    is_continuity = explode()
    
print(ans)