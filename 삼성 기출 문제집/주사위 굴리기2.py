# 10:58~ 
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


# 지도의 세로 크기 n, 가로 크기 m, 이동 하는 횟수 k
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
# 시계 방향 : (d + 1) % 4
# 반시계 방향 : (d + 3) % 4
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_direction(d):
    if d in (0, 1):
        d += 2
    elif d in (2, 3):
        d -= 2
    return d

# rotate: 시계 방향이면 0, 반시계 방향이면 1
def rotate_direction(d, rotate):
    # 시계 방향
    if not rotate:
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4
        
    return d
        
    
# 가장 처음에 주사위가 놓여져 있는 좌표
x, y = 0, 0

# 가장 처음에 주사위 이동 방향은 동쪽
d = 1

def bfs(x, y, key):
    result = 0
    
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        result += key
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == key:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return result        
    

def roll_dice(d, dice):
    new_dice = deepcopy(dice)
    
    # 북
    if d == 0:
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]
        
    # 동
    elif d == 1:
        new_dice[0] = dice[3]
        new_dice[2] = dice[0]
        new_dice[3] = dice[5]
        new_dice[5] = dice[2]
        
    # 남
    elif d == 2:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
        
    # 서
    else:
        new_dice[0] = dice[2]
        new_dice[2] = dice[5]
        new_dice[3] = dice[0]
        new_dice[5] = dice[3]
        
    return new_dice
        
    
    


score =  0
dice = [1, 2, 3, 4, 5, 6]
for idx in range(k):
    # 주사위가 이동 방향으로 한 칸 굴러간다. 
    nx, ny = x + dx[d], y + dy[d]
    # 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    if not (0 <= nx < n and 0 <= ny < m):
        d = change_direction(d)
        nx, ny = x + dx[d], y + dy[d]
    x, y  = nx, ny    
    
    dice = roll_dice(d, dice)
        
    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    score += bfs(x, y, graph[x][y])
    
    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    A, B = dice[5], graph[x][y]

    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    if B < A:
        d = rotate_direction(d, 0)
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    elif A < B:
        d = rotate_direction(d, 1)
        
    
print(score)
    
        
    
    
    
    
    
    
    
    