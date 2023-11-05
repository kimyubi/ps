import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 31
dp[1], dp[2] = 0, 3

for i in range(3, 31):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 
        
print(dp[n])