import sys
input = sys.stdin.readline

# 수열의 크기 n
n = int(input())
sequence = list(map(int, input().split()))
dp = [[x] for x in sequence]

for i in range(n):
    tmp = list()
    for j in range(i):
        if sequence[j] < sequence[i]:
            if len(tmp) < len(dp[j]):
                tmp = dp[j]
                
    dp[i] = tmp[:]
    dp[i].append(sequence[i])
    
dp.sort(key=lambda x : len(x))
result = dp[-1]
print(len(result))
print(*result)