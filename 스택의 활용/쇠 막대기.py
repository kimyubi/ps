sign = input()
stack = []
result = 0

for i in range(len(sign)):
    if sign[i] == "(":
        stack.append(sign[i])
    
    else:
        stack.pop()
        if sign[i-1] == "(":
            result += len(stack)
        else:
            result += 1
print(result)
