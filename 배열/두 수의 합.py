n = int(input())
nums = list(map(int, input().split()))
x = int(input())

l = [0] * 2000001
result = 0

for num in nums:
    if (x-num > 0) and (l[x-num] == 1):
        result += 1
            
    l[num] = 1

print(result)
    