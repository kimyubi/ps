from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
paint = [list(input().rstrip()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

rg_blinds_visited = [[False] * N for _ in range(N)]
general_visited = [[False] * N for _ in range(N)]

# 적록색약이 아닌 사람 bfs
def general_bfs(x,y,v):
    queue = deque([(x,y)])
    general_visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if paint[nx][ny] == v and not general_visited[nx][ny]:
                    general_visited[nx][ny] = True
                    queue.append((nx,ny))
    
    
# 적록색약인 사람 bfs
def rg_blinds_bfs(x,y,v):
    queue = deque([(x,y)])
    rg_blinds_visited[x][y] = True
    
    if v == 'B':
        while queue:
            x, y = queue.popleft()
        
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
            
                if 0 <= nx < N and 0 <= ny < N:
                    if paint[nx][ny] == v and not rg_blinds_visited[nx][ny]:
                        rg_blinds_visited[nx][ny] = True
                        queue.append((nx,ny))
                        
    elif v in ('R','G'):
        while queue:
            x, y = queue.popleft()
        
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
            
                if 0 <= nx < N and 0 <= ny < N:
                    if paint[nx][ny] in ('R','G') and not rg_blinds_visited[nx][ny]:
                        rg_blinds_visited[nx][ny] = True
                        queue.append((nx,ny))

# 적록색약이 아닌 사람이 봤을 때 구역의 수를 구하는 코드
general_cnt = 0
for i in range(N):
    for j in range(N):
        if not general_visited[i][j]:
            general_bfs(i,j,paint[i][j])
            general_cnt += 1
                
# 적록색약인 사람이 봤을 때 구역의 수를 구하는 코드
rg_blinds_cnt = 0
for i in range(N):
    for j in range(N):
        if not rg_blinds_visited[i][j]:
            rg_blinds_bfs(i,j,paint[i][j])
            rg_blinds_cnt += 1
                
print(general_cnt, rg_blinds_cnt)
                                   
                
        
        