from itertools import permutations
def is_prime_number(item):
    if item < 2:
        return False
    
    for i in range(2, int(item ** 0.5) + 1):
        if item % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    group = set()
    
    for i in range(len(numbers)):
        for x in permutations(numbers, i+1):
            group.add(int("".join(x)))

    for item in group:
        if is_prime_number(item):
            answer += 1
            
    return answer