import sys
input = sys.stdin.readline

# n: 계단의 개수
n = int(input())

# 각 계단에 쓰여 있는 점수 입력받기
score = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

def solution():
    if n == 1:
        return score[1]
    if n == 2:
        return score[1] + score[2]
    
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    
    for i in range(3, n+1):
        dp[i] = max(score[i-1] + score[i] + dp[i-3], dp[i-2] + score[i])
    
    return dp[n]


print(solution())