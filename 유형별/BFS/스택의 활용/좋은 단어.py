N = int(input())
sum = 0

for _ in range(N):
    sentence = input()
    stack = []
    
    for c in sentence:
        if not stack:
            stack.append(c)
            continue
        
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        sum += 1 
        
        
print(sum)