import sys
input = sys.stdin.readline

# 기관차가 끌고 가던 객차의 수
n = int(input())
coach = [0] + list(map(int, input().split()))
max_amount = int(input())

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, n + 1):
    coach[i] += coach[i - 1]
    
for i in range(1, 4):
    for j in range(max_amount, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_amount] + coach[j] - coach[j - max_amount])

print(dp[-1][-1])
