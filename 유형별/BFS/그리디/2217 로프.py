import sys
from collections import deque

input = sys.stdin.readline

# 로프의 개수 n
n = int(input())

# 로프의 최대 중량
w =[int(input()) for _ in range(n)]
w.sort()
w = deque(w)

candidates = []

while w:
    x = len(w)
    candidates.append(w.popleft() * x)
        
print(max(candidates))