import sys

input = sys.stdin.readline

# 집의 개수
n = int(input())

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용
cost = [list(map(int, input().split())) for _ in range(n)]

# 빨강 0, 초록 1, 파랑 2
for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))