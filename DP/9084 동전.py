import sys

input = sys.stdin.readline

# 테스트 케이스의 개수 t
t = int(input())
    
    
for _ in range(t):
    # 동전의 가지 수 n
    n = int(input())
    
    # n가지 동전의 각 금액이 오름차 순으로 정렬되어 주어진다.
    coins =  list(map(int, input().split()))
    
    # 주어진 n가지 동전으로 만들어야 할 금액
    m = int(input())
    
    dp = [0] * (m+1)
    dp[0] = 1
    
    for c in coins:
        for i in range(1, m+1):
            if i - c >= 0:
                dp[i] += dp[i-c]
                
                
    print(dp[m])