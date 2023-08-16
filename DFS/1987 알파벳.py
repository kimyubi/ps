import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 세로 r칸, 가로 c칸
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

ans = 0
def dfs(x, y, cnt, record):
    global ans
    
    if (x < 0 or x >= r or y < 0 or y >= c) or board[x][y] in record:
        ans = max(ans, cnt)
        return 
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, cnt + 1, record + board[x][y])
    
dfs(0, 0, 1, '')
print(ans -1)