import sys
from copy import deepcopy

input = sys.stdin.readline

# 지도의 세로 크기 n, 가로 크기 m / 주사위를 놓은 곳의 좌표 x,y / 명령의 개수 k
n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
# (0, 윗면, 뒷 옆면, 오른쪽 옆면, 왼쪽 옆면, 앞쪽 옆면, 바닥면)
dice = [0] * 7

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
command = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, -0, 0]

def roll(direction):
    global dice, graph
    global x,y
   
    nx, ny = x + dx[direction-1], y + dy[direction-1]
   
    # 주사위를 굴렸을 때 바깥으로 이동시키려고 하는 경우 해당 명령을 무시 
    if 0 <= nx < n and 0 <= ny < m:    
        origin_dice = deepcopy(dice)
    
        tmp = [0] * 7
        
        # 동쪽으로 굴리기
        if direction == 1:
            y += 1
            
            tmp[1] = origin_dice[4]
            tmp[2] = origin_dice[2]
            tmp[3] = origin_dice[1]
            tmp[4] = origin_dice[6]
            tmp[5] = origin_dice[5]
            tmp[6] = origin_dice[3]
        
        # 서쪽으로 굴리기
        elif direction == 2:
            y -= 1
            
            tmp[1] = origin_dice[3]
            tmp[2] = origin_dice[2]
            tmp[3] = origin_dice[6]
            tmp[4] = origin_dice[1]
            tmp[5] = origin_dice[5]
            tmp[6] = origin_dice[4]
            
        # 북쪽으로 굴리기
        elif direction == 3:
            x -= 1
 
            tmp[1] = origin_dice[5]
            tmp[2] = origin_dice[1]
            tmp[3] = origin_dice[3]
            tmp[4] = origin_dice[4]
            tmp[5] = origin_dice[6]
            tmp[6] = origin_dice[2]
            
        # 남쪽으로 굴리기
        elif direction == 4:
            x += 1
        # (0, 윗면, 뒷 옆면, 오른쪽 옆면, 왼쪽 옆면, 앞쪽 옆면, 바닥면)
            tmp[1] = origin_dice[2]
            tmp[2] = origin_dice[6]
            
            tmp[3] = origin_dice[3]
            tmp[4] = origin_dice[4]
            
            tmp[5] = origin_dice[1] 
            tmp[6] = origin_dice[5] 
            
        
        dice = tmp

        if graph[x][y] == 0:
            graph[x][y] = dice[6]
        else:
            dice[6] = graph[x][y]
            graph[x][y] = 0
   
        print(dice[1])
            
            
def solution():
    for com in command:
        roll(com)

solution()