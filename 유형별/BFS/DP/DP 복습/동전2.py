import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

# dp[i] : 가치의 합이 i일때 동전의 최소 개수
dp = [0] + [10001] * k

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin]  + 1)
        
if dp[k] == 10001:
       print(-1)
else:
   print(dp[k])