# 12:50 ~
import sys
from copy import deepcopy
input = sys.stdin.readline

# 위, 아래, 오른쪽, 왼쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

# 격자판의 크기 r * c, 상어의 수 m
r, c, m = map(int, input().split())

board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1].append([s, d, z])

# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
pointer = -1
answer = 0

for t in board:
    print(t)

while True:
    # 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
    pointer += 1
    
    if pointer == c:
        break

    # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for idx in range(r):
        if board[idx][pointer]:
            answer += board[idx][pointer][0][-1]
            board[idx][pointer][0].clear()
            break
        
    # 상어가 s칸 이동한다.
    # 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
    visited = []
    for x in range(r):
        for y in range(c):
            if board[x][y]:
                if board[x][y][0]:
                    sx, sy = x, y
                    s, d, z = board[x][y][0]
                    if z in visited:
                        continue
                    cnt = 0
                    while True:
                        if cnt == s:
                            ps, pv, pz = board[sx][sy].pop()
                            board[x][y].append([ps, d, pz])
                            visited.append(pz)
                            break
                        
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < r and 0 <= ny < c:
                            cnt += 1
                            x, y = nx, ny
                            
                        # 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
                        else:
                            # 위, 아래, 오른쪽, 왼쪽
                            if d == 1:
                                d = 2
                                continue
                            elif d == 2:
                                d = 1
                                continue
                            elif d == 3:
                                d = 4
                                continue
                            else:
                                d = 3
                                continue
    
    print(pointer)           
    for t in board:
        print(t)
        
    print()
                              
    
    # 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.   
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                if 2 <= len(board[i][j]):
                    board[i][j].sort(key=lambda x: x[-1])
                        
                    for idx in range(len(board[i][j]) -1):
                        board[i][j][-1][-1] += board[i][j][idx][-1]
                        
                    larges_shark = board[i][j][-1]
                    
                    board[i][j].clear()
                    board[i][j].append(larges_shark)             
                    
                    
    
                
print(answer)
            
                
