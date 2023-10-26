import sys
input = sys.stdin.readline

# 미로의 크기
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
candy = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i][j] 
        
print(dp[n][m])