import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i,N):
        if i < j:
            dp[i][j] = float("inf")
            for cut in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][cut] + dp[cut+1][j] +
                            matrix[i][0]*matrix[cut][1]*matrix[j][1])        

print(dp[0][-1])