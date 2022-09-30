import sys


input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for size in range(1, n):
    for start in range(n - size):
        end = start + size
        
        result = float("inf")
        for cut in range(start, end):
            result = min(result, dp[start][cut] + dp[cut + 1][end] + matrix[start][0] * matrix[cut][1] * matrix[end][1])
            
        dp[start][end] = result
        

print(dp[0][-1])
            