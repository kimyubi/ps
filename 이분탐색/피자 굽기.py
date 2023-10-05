import sys
from collections import deque
input = sys.stdin.readline

# 오븐의 깊이 d, 피자 반죽의 개수 n
d, n = map(int, input().split())
ovens = list(map(int, input().split()))
doughs = list(map(int, input().split())) 

for i in range(d-1):
    if ovens[i] < ovens[i + 1]:
        ovens[i + 1]  = ovens[i]
        
ovens = deque(ovens[::-1])

result = []
depth = d + 1

for dough in doughs:
    while ovens:
        depth -= 1
        x = ovens.popleft()
        
        if x >= dough:
            result.append(depth)
            break
        
if len(result) != n:
    print(0)
else:
    print(result[-1])
        
    

