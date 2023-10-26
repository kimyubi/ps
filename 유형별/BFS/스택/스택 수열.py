N = int(input())

stack = []
result = []
current = 1
flag = True

for _ in range(N):
    num = int(input())
    
    while current <= num:
        stack.append(current)
        current += 1
        result.append("+")
    
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    
    else:
        flag = False
    

if flag:
    for i in result:
        print(i)
else:
    print("NO")        
        
    