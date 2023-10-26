from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = sys.maxsize


dx = [-1,1,0,0]
dy = [0,0,-1,1]



# 섬 구분하기
def seperate_island(x,y,temp):
    queue = deque([(x,y)])
    visited[x][y] = True
    graph[x][y] = temp
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = temp
                    queue.append((nx,ny))       

temp = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            seperate_island(i,j,temp)
            temp += 1


# 다리 만들기           
def bfs(cnt):
    global answer
    dist = [[-1] * n for _ in range(n)]     
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == cnt:
                queue.append((i,j))
                dist[i][j] == 0
                
    while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
            
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0 and graph[nx][ny] != cnt:
                        answer = min(answer, dist[x][y] + 1)
                        return
            
                    if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
                
    

for i in range(1,temp):
    bfs(i)


print(answer)



            


        

