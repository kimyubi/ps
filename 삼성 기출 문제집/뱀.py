import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 보드의 크기 n
n = int(input())
# 빈칸 0, 사과 1, 뱀 2
board = [[0] * (n) for _ in range(n)]

# 사과의 개수 k
k = int(input())
for _ in range(k):
    r,c = map(int, input().split())
    board[r-1][c-1] = 1
    
# 뱀의 방향 변환 횟수 l
l = int(input())
command = defaultdict(int)
for _ in range(l):
    x, c = input().split()
    command[int(x)] = c
        

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction + 3) % 4 
    else:
        direction = (direction + 1) % 4 
    
cnt = 0
nx, ny, direction = 0, 0, 1
snake = deque()
snake.append((0,0))

while True:
    cnt += 1
    nx, ny = nx + dx[direction], ny + dy[direction]
    
    # 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
        break
    
    # 사과가 있다면
    if board[nx][ny]:
        board[nx][ny] = 2
        snake.append((nx, ny))
        
        if cnt in command.keys():
            turn(command[cnt])
                
    elif not board[nx][ny]:
        board[nx][ny] = 2
        snake.append((nx, ny))
        
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        
        if cnt in command.keys():
            turn(command[cnt])
            
                
print(cnt)
        
                
            
        
    
    
        
        
    
                
        
    
    