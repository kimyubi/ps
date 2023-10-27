import sys
from collections import deque
input = sys.stdin.readline

# 보드의 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
def init():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    
def move(x, y, dx, dy):
    # 이동 칸 수
    cnt = 0
    
    # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아니면 계속 이동할 수 있다.
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        
    return x, y, cnt 
 
def solution():
    init()
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        
        if 10 < depth:
            return -1
            
        
        for i in range(4):
            nrx, nry, r_cnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_cnt = move(bx, by, dx[i], dy[i])
            
            # 파란 구슬이 구멍에 빠지지 않고
            if board[nbx][nby] != 'O':
                # 빨간 구슬이 구멍에 빠지면 성공
                if board[nrx][nry] == 'O':
                    return depth
            
                # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
                if (nrx, nry) == (nbx, nby):
                    if r_cnt < b_cnt:
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]
                        
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))
                
    return -1


print(solution())                
                