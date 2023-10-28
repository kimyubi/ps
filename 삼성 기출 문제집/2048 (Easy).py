import sys
from copy import deepcopy
input = sys.stdin.readline

# 보드의 크기 n
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 한번의 이동 : 보드 위에 있는 전체 블록을 상하좌우 네방향중 하나로 이동
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐진다.
# 한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 합쳐질 수 없다.
# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

def move(board, direction):
    # 왼쪽으로 이동
    if direction == 0:
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
    if direction == 1:
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
                        
    
    # 위쪽으로 이동
    if direction == 2:
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
                        
                
    # 아래쪽으로 이동
    if direction == 3:
        for j in range(n):
            pointer = n-1
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
                
                

answer = 0  
def solution(board, depth):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, board)))
        return
        
    for i in range(4):
        solution(move(deepcopy(board), i), depth + 1)
        
solution(board, 0)    
print(answer)
        
    
                
            
            
            