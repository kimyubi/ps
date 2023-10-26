import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도의 크기 n
n = int(input())
map = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    if map[x][y] == 1:
        global cnt
        cnt += 1
        map[x][y] = 0
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)

cnt = 0
ans = []       
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
print(*ans, sep='\n')
