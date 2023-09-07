import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대나무 숲의 크기 n
n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and info[x][y] < info[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
            
    return dp[x][y]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
        
print(result)