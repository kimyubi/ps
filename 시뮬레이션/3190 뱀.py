# 20: 40
import sys
from collections import deque

input = sys.stdin.readline

# 보드의 크기 (n x n)
n = int(input())

# 뱀 -1, 빈 칸 0, 사과 1
board = [[0] * n for _ in range(n)]
board[0][0] = -1
r, y = 0, 0
d = 1


# 사과의 갯수
k = int(input())

# 보드에 사과의 위치 표시
for _ in range(k):
    i,j = map(int, input().split())
    board[i][j] = 1
    
    
# 뱀의 방향 전환 횟수
l = int(input())

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]



# 왼쪽으로 90도 회전 (d+3)%4
# 오른쪽으로 90도 회전 (d+1)%4
turnabout = deque()

for _ in range(l):
    
    # 정수 x,  문자 c
    # 게임 시작 시간으로부터 x초가 끝난 뒤에 왼쪽(c==l) 또는 오른쪽(c==d)으로 90도 방향을 회전시킨다는 뜻이다.
    x, c = input().split()
    turnabout.append([int(x),c])
    
time = 0

def solution(r,y,d):
    global time
    last_x,last_y,last_d = 0,0,0
    start = 0
    while turnabout:
        x,c = turnabout.popleft()
        print(start,x,d)
        
        for b in board:
            print(b)
        for _ in range(start, x):
            nr, ny = r + dx[d], y + dy[d]
            time += 1
            if 0 <= nr < n and 0 <= ny < n:
                # 뱀이 기어다니다가 자기자신의 몸과 부딪히면 게임이 끝난다.
                if board[nr][ny] == -1:
                    return
                
                if board[nr][ny] == 1:
                    board[nr][ny] = -1
                    
                if board[nr][ny] == 0:
                    board[nr][ny] = -1
                    board[r][y] = 0
            
                r,y = nr, ny
                start = x
                last_x, last_y = r,y
                
                
             
            # 뱀이 기어다니다가 벽과 부딪히면 게임이 끝난다.
            else:
                return
                
        
        if c == 'L':
            d = (d+3)%4
            
        elif c == 'D':
            d = (d+1)%4       
        
        last_d = d  
                    
    
    
    print(last_x,last_y,last_d)
    r,y,d = last_x,last_y,last_d
    print(r,y,d)
    for b in board:
            print(b)
            
    while True:
        nr, ny = r + dx[d], y + dy[d]
        time += 1
        if 0 <= nr < n and 0 <= ny < n:
            # 뱀이 기어다니다가 자기자신의 몸과 부딪히면 게임이 끝난다.
            if board[nr][ny] == -1:
                return
                    
            if board[nr][ny] == 1:
                board[nr][ny] = -1
                        
            if board[nr][ny] == 0:
                board[nr][ny] = -1
                board[r][y] = 0
        
        else:
            return
        
        r,y = nr, ny
        
        for b in board:
            print(b)
                
            
            
            
        
solution(r,y,d)    
print(time)

# 3번테케 안됨