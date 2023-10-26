import math 

def getPrimaryNum_Eratos(n): 
    nums = [True for i in range(n + 1)] 
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums [i]: # i가 소수인 경우 (남은 수인 경우)
            j = 2
            while i * j <= n:
                nums [i * j] = False
                j += 1

    return [i for i in range(2, n) if nums[i]]

n = int(input())

def getFactorization_Eratos(n):
    prime_nums = getPrimaryNum_Eratos(n)
    if n in prime_nums:
        print(n)  # n이 소수라면 소인수분해되지 않으므로 그대로 출력
        return 
    
    for prime_num in prime_nums:
        while(n % prime_num == 0):
            print(prime_num)
            n //= prime_num
    
getFactorization_Eratos(n)