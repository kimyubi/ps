import sys

input = sys.stdin.readline

n = int(input()) 
h = [int(input()) for i in range(n)]
stk = []
result = 0
 
for i in range(n):
    while stk and stk[-1] <= h[i]:
        stk.pop()
    
    result += len(stk) 
    stk.append(h[i])
    
print(result)