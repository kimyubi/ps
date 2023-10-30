import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 보드의 크기 n
n = int(input())
# 뱀 1, 사과 2
board = [[0] * n for _ in range(n)]

# 게임이 시작할 때 뱀음 맨위 맨 좌측에 위치하고 오른쪽을 향한다.
board[0][0] = 1
snake = deque()
snake.append((0, 0))
direction = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사과의 개수 k
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2
    
# 뱀의 방향 변환 횟수 l
command = defaultdict(int)
l = int(input())
for _ in range(l):
    x, c = input().split()
    command[int(x)] = c
    
    
def turn(c):
    global direction
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4
        
    
x, y = 0, 0
time = 0

while True:
    time += 1
    nx, ny = x + dx[direction], y + dy[direction]
    
    if not (0 <= nx < n  and 0 <= ny < n) or board[nx][ny] == 1:
        break
    
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake.append((nx, ny))
        
        if time in command.keys():
            turn(command[time])
    
    # 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다.      
    else:
        board[nx][ny] = 1 
        snake.append((nx, ny))
        
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        
        if time in command.keys():
            turn(command[time])
            
    
    x, y = nx, ny
    
    
print(time)
        
        
        
    