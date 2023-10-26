# 돈을 인출하는 시간이 짧은 순서대로 줄을 서면, 각 사람이 돈을 인출하는데 필요한 시간의 합이 최소가 된다.
import sys

input = sys.stdin.readline
n = int(input())
times = list(map(int, input().split()))

times.sort()

# 각 사람이 돈을 인출하는데 필요한 최소 시간
dp = times

for i in range(1,n):
    dp[i] = dp[i-1] + dp[i]
    
print(sum(dp))