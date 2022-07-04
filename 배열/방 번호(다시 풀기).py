l = [0 for _ in range(10)]
n = input()

for num in n:
    num = int(num)
    
    if num == 6 or num == 9:
        if l[6] <= l[9]:
            l[6] += 1
        
        else:
            l[9] += 1

    else:
        l[num] += 1

result = max(l)
print(result)
