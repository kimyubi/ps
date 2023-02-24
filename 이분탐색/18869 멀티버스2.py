import sys
input = sys.stdin.readline

m, n = map(int, input().split())
result = []

for _ in range(m):
    nums = list(map(int, input().split()))
    origin = nums[::]
    nums.sort()
    
    tmp = list()
    dic = dict()
    for idx, num in enumerate(nums):
        dic[num] = idx
        
    for x in origin:
        tmp.append(dic[x])
        
    result.append(tmp)

ans = 0
for i in range(m):
    for j in range(i+1, m):
        if result[i] == result[j]:
            ans += 1
            
print(ans) 
    
    