import sys
input = sys.stdin.readline

n = int(input())

# 모든 수는 1의 제곱수의 합으로 나타낼 수 있으므로 dp값을 1~n 까지로 초기화한다.
dp = [x for x in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])
        