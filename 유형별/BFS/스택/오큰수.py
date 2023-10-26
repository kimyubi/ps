N = int(input())
A = list(map(int, input().split()))
stack = []
result = []

while A:
    v = A.pop()
    
    while stack:
        if stack and stack[-1] > v:
            result.append(stack[-1])
            break
        else:
            stack.pop()
        
    if not stack:
        result.append(-1)
    stack.append(v)
    
print(*reversed(result))