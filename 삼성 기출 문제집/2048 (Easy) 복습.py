import sys
from copy import deepcopy
input = sys.stdin.readline

# 보드의 크기 n
n = int(input())

# 게임판의 초기 상태 board, 0은 빈 칸 / 이외의 값은 모두 블록
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def move(direction, board):
    # 왼쪽으로 이동
    if direction == 1:
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if not board[i][pointer]:
                        board[i][pointer] = tmp
                        
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                        
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    
    # 오른쪽으로 이동
    elif direction == 2:
        for i in range(n):
            pointer = n - 1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if not board[i][pointer]:
                        board[i][pointer] = tmp
                        
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
                        
                
        
    # 위로 이동
    elif direction == 3:
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if not board[pointer][j]:
                        board[pointer][j] = tmp
                        
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                        
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
                
    # 아래로 이동
    else:
        for j in range(n):
            pointer = n - 1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if not board[pointer][j]:
                        board[pointer][j] = tmp
                        
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    
    return board
    
def solution(depth, board):
    global answer 
    
    if depth == 5:
        answer = max(answer, max(map(max, board)))
        return
    
    for i in range(4):
        solution(depth + 1, move(i, deepcopy(board)))

solution(0, board)
print(answer)