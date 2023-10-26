import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


# 빨간 공(rx,ry)와 파란 공(bx,by)의 방문 체크
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def set_position():
    rx, ry, bx, by = 0, 0, 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j]  == 'R':
                rx, ry = i, j
            
            elif board[i][j] == 'B':
                bx, by = i, j
                
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    
    # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아니면 계속 이동
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        
    return x, y, cnt


def solution():
    set_position()
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        
        # 실패 조건
        if depth > 10:
            break
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
    
            # 파란 공이 구멍에 빠지지 않고
            if board[nbx][nby] != 'O':
                # 빨간 공이 구멍에 빠졌으면 성공
                if board[nrx][nry] == 'O':
                    print(depth)
                    return
            
                # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.     
                if nrx == nbx and nry == nby:
                    
                    # 이동거리가 더 큰 구슬을 한 칸 뒤로
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                        
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                        
                # 방문 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))
                    
    print(-1)           
    
solution()
        
    
    