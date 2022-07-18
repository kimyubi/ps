import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int,input().split()))
result = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    
    if not stack:
        result.append(0)
    stack.append([i, tower[i]])
            
print(*result)