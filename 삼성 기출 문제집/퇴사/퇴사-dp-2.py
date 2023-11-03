import sys
input = sys.stdin.readline

# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
N = int(input())
T, P = [], []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N + 1)

for i in range(N):
    if N < i + T[i]:
        continue
    
    dp[i] = max(dp[:i + 1])
    dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
    

print(max(dp))
