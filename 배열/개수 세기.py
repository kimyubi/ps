from collections import Counter

result = 0

n = int(input())
l = list(map(int,input().split()))
v = int(input())

counter = Counter(l)

if v in counter:
    result = counter[v]
    

print(result)
    
    


    
       
