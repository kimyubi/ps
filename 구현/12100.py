# 오후 3시 31분부터
# 전체 블록을 상/하/좌/우로 각각 이동시키는 함수를 만든다.
# 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐진다.
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구한다  == 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구한다.  

from copy import deepcopy
import sys

input = sys.stdin.readline
n = int(input()) # 보드의 크기
board = [list(map(int, input().split())) for _ in range(n)] # 게임판의 초기 상태

ans = 0

def left(board):
    for i in range(n):
        x, position = 0, 0
        for j in range(n):
            
            if board[i][j] == 0:
                continue
            
            if x == 0:
                x = board[i][j]
            
            else:
                # 블록이 합쳐질 수 있으면
                if x == board[i][j]:           
                    board[i][position] = x * 2 # 블록 합치기
                    x = 0                      # x 초기화
                    position += 1
                    
                else:
                    board[i][position] = x
                    x = board[i][j]
                    position += 1
            
            board[i][j] = 0
        
        if x != 0:
            board[i][position] = x
            
    return board

def right(board):
    for i in range(n):
        x, position = 0, n-1
        for j in range(n-1, -1, -1):
            if board[i][j] == 0:
                continue
            
            if x == 0:
                x = board[i][j]
            else:
                if x == board[i][j]:
                    board[i][position] = x * 2
                    x = 0
                    position -= 1
                    
                else:
                    board[i][position] = x
                    x = board[i][j]
                    position -= 1
                    
            
            board[i][j] = 0
    
        if x != 0:
            board[i][position] = x       
            
    return board     
                    
    
def up(board):
    for i in range(n):
        x, position = 0, 0
        for j in range(n):
            if board[j][i] == 0:
                continue
            
            if x == 0:
                x = board[j][i]
            
            else:
                # 블록이 합쳐질 수 있으면
                if x == board[j][i]:           
                    board[position][i] = x * 2 # 블록 합치기
                    x = 0                      # x 초기화
                    position += 1
                    
                else:
                    board[position][i] = x
                    x = board[j][i]
                    position += 1
            
            board[j][i] = 0
        
        if x != 0:
            board[position][i] = x
            
    return board
    
    
def down(board):
    for i in range(n):
        x, position = 0, n-1
        for j in range(n-1, -1, -1):
            if board[j][i] == 0:
                continue
            
            if x == 0:
                x = board[j][i]
            else:
                if x == board[j][i]:
                    board[position][i] = x * 2
                    x = 0
                    position -= 1
                    
                else:
                    board[position][i] = x
                    x = board[j][i]
                    position -= 1
                    
            
            board[j][i] = 0
    
        if x != 0:
            board[position][i] = x    
            
    return board


def dfs(depth, tmp_board):
    global ans
    
    if depth == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, tmp_board[i][j])
        return
    
    dfs(depth + 1, left(deepcopy(tmp_board)))
    dfs(depth + 1, right(deepcopy(tmp_board)))
    dfs(depth + 1, up(deepcopy(tmp_board)))
    dfs(depth + 1, down(deepcopy(tmp_board)))
        
dfs(0, board)
print(ans)

