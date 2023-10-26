import sys 
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 공간의 크기 n
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
time, size, cnt = 0, 2, 0

# 아기 상어의 위치 구하기
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            sx, sy = i, j
   
def bfs():
    global sx, sy, size, cnt
    
    queue = deque()
    queue.append([sx, sy])
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    fish = []
    
    while queue:
        x, y = queue.popleft()  
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 빈 칸이거나, 크기가 같은 물고기일 경우 그냥 지나간다.
                if space[nx][ny] in (0, size):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    continue
                
                # 작은 물고기인 경우
                if space[nx][ny] < size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    fish.append([nx, ny, visited[nx][ny]])
                    continue
    
    if fish:
        space[sx][sy] = 0
        fish.sort(key=lambda x : (x[2], x[0], x[1]))     
        sx, sy, dist = fish[0]
        space[sx][sy] = 9
        cnt += 1
        return dist      
    
while True:
    tmp = bfs()
    if tmp == None:
        break
    
    time += tmp
    if cnt == size:
        size += 1
        cnt = 0
print(time)