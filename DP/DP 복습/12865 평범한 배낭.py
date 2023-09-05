import sys
input = sys.stdin.readline

# 물품의 수 n, 준서가 버틸 수 있는 무게 k
n, k = map(int, input().split())

wv = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = wv[i][0], wv[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
            
print(max(dp[-1]))