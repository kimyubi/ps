import sys
input = sys.stdin.readline

# 수열의 크기 n
n = int(input())
sequence = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    max_value = 0
    for j in range(i):
        if sequence[j] < sequence[i]:
            max_value = max(max_value, dp[j])
            
    dp[i] = max_value + 1
    
print(max(dp))