import sys
from collections import defaultdict

input = sys.stdin.readline

# 배열의 크기 n
n = int(input())

def solution(n):
    ab = defaultdict(int)
    A, B, C, D = [], [], [], []

    for _ in range(n):
        a, b, c, d = map(int, input().split())
        
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    
    for a in A:
        for b in B:
            ab[a+b] += 1
            
    ans = 0
    for c in C:
        for d in D:
            x = -(c+d)
            
            if x in ab:
                ans += ab[x] 
    
    return ans
            
print(solution(n))