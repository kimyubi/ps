# 5:39 ~
import sys
from collections import deque
input = sys.stdin.readline

# 공간의 크기 n
n = int(input())

# 공간의 상태 graph
# 0: 빈 칸
# 1 ~ 6: 칸에 있는 물고기의 크기
# 9 : 아기 상어의 위치
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j

time = 0
size = 2

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    
    fish = []
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    
                    if 0 < graph[nx][ny] < size:
                        fish.append([visited[nx][ny], nx, ny])
                        
    if not fish:
        return False
                        
    fish.sort(key=lambda x: (x[0], x[1], x[2]))
    return fish

cnt = 0
while True:
    exist_eatable_fish = bfs(sx, sy)
    if not exist_eatable_fish:
        break
    
    distance, target_x, target_y = exist_eatable_fish[0]
    
    graph[sx][sy] = 0
    graph[target_x][target_y] = 0
    sx, sy = target_x, target_y
    cnt += 1
    
    # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
    if cnt == size:
        size += 1
        cnt = 0
    
    time += (distance -1)
    
print(time)