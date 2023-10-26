import sys 
input = sys.stdin.readline


# 학생들의 수 n, 두 학생 키를 비교한 횟수 m
n, m = map(int, input().split())

dp = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    # 번호가 a인 학생이 번호가 b인 학생보다 키가 작다.
    # a에서 b로 화살표를 그려서 표현하였다.
    a, b = map(int, input().split())
    dp[a][b] = True
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if dp[a][b] or (dp[a][k] and dp[k][b]):
                dp[a][b] = True
                
result = 0            
for i in range(1, n + 1):
    cnt = dp[i].count(True)
    for j in range(1, n + 1):
        if dp[j][i]:
            cnt += 1
    
    if cnt == n - 1:
        result += 1

