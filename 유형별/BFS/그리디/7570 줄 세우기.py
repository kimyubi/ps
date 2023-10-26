import sys

input = sys.stdin.readline

# 어린이 수 n
n = int(input())
kids = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[kids[i]] = dp[kids[i] -1] + 1

print(n - max(dp))