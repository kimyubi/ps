import sys
input = sys.stdin.readline

# 테스트케이스의 개수 t
t = int(input())

for _ in range(t):
    # 날의 수 n
    n = int(input())
    price = list(map(int, input().split()))
    max = price[-1]
    
    answer = 0
    for i in range(n-2, -1, -1):
        if price[i] < max:
            answer += max - price[i]
        
        else:
            max = price[i]
    
    print(answer)