import sys

input = sys.stdin.readline

# 수의 개수 n, 합을 구해야 하는 횟수 m
n, m = map(int, input().split())

numbers = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

dp[1] = numbers[1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + numbers[i]
        
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]- dp[i-1])
