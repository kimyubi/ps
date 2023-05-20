def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def base_change(n, k):
    # 10진수를 k진수로 변환
    tmp = ''
    while n:
        n, mod = divmod(n, k)
        tmp += str(mod)
        
    return tmp[::-1]

def solution(n, k):
    answer = -1

    tmp = base_change(n, k)

    candidate = tmp.split('0')
    
    prime = []
    for c in candidate:
        if c != '' and is_prime(c):
            prime.append(c)

    return len(prime)

    