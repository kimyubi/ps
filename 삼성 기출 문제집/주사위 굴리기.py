import sys
from copy import deepcopy
input = sys.stdin.readline

# 지도의 세로 크기 n, 가로 크기 m, 주사위를 놓은 곳의 좌표 x, y, 명령의 개수 k
n, m, x, y, k = map(int, input().split())

# 위, 뒤, 오른쪽, 왼쪽, 앞, 아래
dice = [0 for _ in range(6)]
graph = [list(map(int, input().split())) for _ in range(n)]    

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def move(dx, dy):
    global x, y
    global dice, graph
    
    if not (0 <= x + dx < n and 0 <= y + dy < m):
        return
    
    
    x, y = x + dx, y + dy
    new_dice = deepcopy(dice)
    
    # 동쪽으로 이동
    if command == 1:
        new_dice[0] = dice[3]
        new_dice[2] = dice[0]
        new_dice[3] = dice[5]
        new_dice[5] = dice[2]
        
    # 서쪽으로 이동
    elif command == 2:
        new_dice[0] = dice[2]
        new_dice[2] = dice[5]
        new_dice[3] = dice[0]
        new_dice[5] = dice[3]
        
    # 북쪽으로 이동
    elif command == 3:
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]
        
    # 남쪽으로 이동
    else:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]


    dice = new_dice        
    # 이동한 칸에 쓰여있는 수가 0이면 주사위의 바닥면에 쓰여있는 수가 칸에 복사된다.
    if not graph[x][y]:
        graph[x][y] = dice[5]
            
    # 0이 아닌 경우 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사된다.
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0
        
    print(dice[0])
    
for command in list(map(int, input().split())):
    move(dx[command], dy[command])