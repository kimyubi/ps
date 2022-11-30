n = int(input())

stairs = [0] * (301)
dp = [0] * (301)

ans = 0

for i in range(1, n + 1):
    stairs[i] = int(input())

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    # 마지막 계단의 바로 전 계단을 밟은 경우와, 밟지 않은 경우
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
    
print(dp[n])