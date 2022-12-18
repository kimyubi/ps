import sys

input = sys.stdin.readline

# n+1일째 퇴사
n = int(input())
tp = [[]]
dp = [0] * (n+1)

for _ in range(n):
    t, p = map(int, input().split())
    tp.append([t,p])

for i in range(1, n+1):
    if i + tp[i][0] -1 >= n + 1:
        break
    
    max_cost = 0
    for j in range(1, i):
        if tp[j][0] + j - 1 < i:
            max_cost = max(max_cost, dp[j])
    
    dp[i] = tp[i][1] + max_cost
    
print(max(dp))
            
            
        


