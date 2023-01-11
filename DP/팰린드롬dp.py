import sys
input = sys.stdin.readline

# 자연수 n
n = int(input())
numbers = list(map(int, input().split()))

# 질문의 개수 m
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range (n)]

for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len    
        if dp[start][end]:
            continue
        
        if start == end:
            dp[start][end] = 1
            continue
        
        if numbers[start] == numbers[end]:
            if start + 1 == end:
                dp[start][end] = 1
            
            elif dp[start+1][end-1]:
                dp[start][end] = 1
                    
                

for i in range(m):
    s, e = q[i]
    print(1 if dp[s-1][e-1] == 1 else 0)
                

            