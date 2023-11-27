# 12 : 37 ~ 3: 14
import sys
from collections import defaultdict
input = sys.stdin.readline

# 북 남 서 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def minus(x):
    return x - 1

# 격자의 크기 n, 상어의 수 m, 냄새 지속 수 k
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

sharks = defaultdict(list)
for i in range(n):
    for j in range(n):
        if data[i][j]:
            sharks[data[i][j]] = [i, j]
            
sharks_directions = list(map(int, input().split()))
for idx, direction in enumerate(sharks_directions):
    sharks[idx + 1].append(direction -1)
    
priority = defaultdict(list)
for shark_index in range(1, m + 1):
    tmp = []
    for shark_direction in range(4):
        tmp.append(list(map(minus, map(int, input().split()))))
    priority[shark_index].extend(tmp)

graph = [[None] * n for _ in range(n)]
def diminish_smell():
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                graph[i][j][1] -= 1
                    
                if not graph[i][j][1]:
                    graph[i][j] = None

def spread_smell():
    for shark in sharks.keys():   
        if shark in removed_shark:
            continue
        
        x, y, d = sharks[shark]
        if not graph[x][y]:
            graph[x][y] = [shark, k]
        else:
            origin = graph[x][y][0]
            if origin == shark:
                graph[x][y] = [shark, k]
                
            else:
                if shark < origin:
                    graph[x][y] = [shark, k]
                removed_shark.append(max(origin, shark))

def move_shark():
    for shark in sharks.keys():
        if shark in removed_shark:
            continue
        x, y, d = sharks[shark]
        exist_empty_smell_room = False    
        for direction in priority[shark][d]:
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n:
                # 아무 냄새가 없는 칸으로 이동한다.
                if not graph[nx][ny]:
                    sharks[shark] = [nx, ny, direction]
                    exist_empty_smell_room = True
                    break
        
        if not exist_empty_smell_room:
            for direction in priority[shark][d]:
                nx, ny = x + dx[direction], y + dy[direction]
                if 0 <= nx < n and 0 <= ny < n:
                    # 그러한 칸이 없으면 자신의 냄새가 있는 칸으로 이동한다.
                    if graph[nx][ny][0] == shark:
                        sharks[shark] = [nx, ny, direction]
                        break

removed_shark = []
time = -1
while True:
    if len(removed_shark) == m - 1:
        break
    if 1000 <= time:
        time = -1
        break
    time += 1
    spread_smell()
    move_shark()
    diminish_smell()   
    
        
print(time)
