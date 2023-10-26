import sys
from copy import deepcopy

input = sys.stdin.readline

# 보드의 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

result = sys.maxsize 

# direction: 0(왼쪽), 1(오른쪽), 2(위), 3(아래)
def move(board, direction):
    
    # 왼쪽으로 기울이기
    if direction == 0:
        # 가장 바깥 행은 모두 막혀 있다.
        for i in range(1, n-1):
            position = 1
            # 가장 바깥 열은 모두 막혀 있다.
            for j in range(1, m-1):
                if position == j or board[i][j] == '.':
                        continue
                
                elif board[i][j] == '#':
                    position = j + 1
                    continue
            
                elif board[i][j] == 'O':
                    position = j
                    continue
                        
                # board[i][j] = R or B
                else:        
                    if board[i][position] == 'O':
                        board[i][j] = '.'
                        
                    elif board[i][position] == '.':
                        board[i][position] = board[i][j]
                        board[i][j] = '.'
                        position += 1
                    
                    else:
                        position += 1
                        
    # 오른쪽으로 기울이기
    if direction == 1:
        # 가장 바깥 행은 모두 막혀 있다.
        for i in range(1, n-1):
            position = m-2
            # 가장 바깥 열은 모두 막혀 있다.
            for j in range(m-2, 0, -1):
                if position == j or board[i][j] == '.':
                        continue
                
                elif board[i][j] == '#':
                    position = j - 1
                    continue
            
                elif board[i][j] == 'O':
                    position = j
                    continue
                        
                # board[i][j] = R or B
                else:        
                    if board[i][position] == 'O':
                        board[i][j] = '.'
                        
                    elif board[i][position] == '.':
                        board[i][position] = board[i][j]
                        board[i][j] = '.'
                        position -= 1
                    
                    else:
                        position -= 1
        
    # 위로 기울이기
    if direction == 2:
        # 가장 바깥 행은 모두 막혀 있다.
        for i in range(1, m-1):
            position = 1
            # 가장 바깥 열은 모두 막혀 있다.
            for j in range(1, n-1):
                if position == j or board[j][i] == '.':
                        continue
                
                elif board[j][i] == '#':
                    position = j + 1
                    continue
            
                elif board[j][i] == 'O':
                    position = j
                    continue
                        
                # board[i][j] = R or B
                else:        
                    if board[position][i] == 'O':
                        board[j][i] = '.'
                        
                    elif board[position][i] == '.':
                        board[position][i] = board[j][i]
                        board[j][i] = '.'
                        position += 1
                    
                    else:
                        position += 1
    
    # 아래로 기울이기
    if direction == 3:
        # 가장 바깥 행은 모두 막혀 있다.
        for i in range(1, m-1):
            position = n-2
            # 가장 바깥 열은 모두 막혀 있다.
            for j in range(n-2, 0, -1):
                if position == j or board[j][i] == '.':
                        continue
                
                elif board[j][i] == '#':
                    position = j - 1
                    continue
            
                elif board[j][i] == 'O':
                    position = j
                    continue
                        
                # board[i][j] = R or B
                else:        
                    if board[position][i] == 'O':
                        board[j][i] = '.'
                        
                    elif board[position][i] == '.':
                        board[position][i] = board[j][i]
                        board[j][i] = '.'
                        position -= 1
                    
                    else:
                        position -= 1    
                           
    return board
                    
def dfs(depth, tmp_board, i):
    global result
    
    if depth <= 10:
        # 파란 구슬이 구멍에 빠지면 실패
        if all('B' not in b for b in tmp_board):
            return
        
        # 빨간 구슬이 구멍에 빠지면 성공
        if all('R' not in b for b in tmp_board):
            result = min(depth, result)
            return
    else:
        return
    
    for direction in range(4):
        if direction == i:
            continue
        
        dfs(depth + 1, move(deepcopy(tmp_board), direction), direction)
        
        
def solution():
    global result
    
    if result <= 10:
        print(result)
    else:
        print(-1)

dfs(0, board, 0)
solution()




