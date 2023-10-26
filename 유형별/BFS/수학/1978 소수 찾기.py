import sys 

n = int(input())
nums = list(map(int, input().split()))

# 소수 : 1과 자기 자신으로 나눌 대만 나누어 떨어지는 자연수 

ans = 0

for num in nums:
    is_prime = True
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                is_prime = False
        
        if is_prime:
            ans += 1
        
print(ans)