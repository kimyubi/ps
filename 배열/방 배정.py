from collections import defaultdict

n, k = map(int, input().split())

male = defaultdict(int)
female = defaultdict(int)

result = 0

for _ in range(n):
    s, y = map(int, input().split())
    
    # 여자
    if s == 0:
        female[y] += 1;
        
    # 남자
    else:
        male[y] += 1;
        
print(male , female)

for v in female.values():
    if v%k == 0:
        result += v//k
    else:
        result += v//k + 1
    
for v in male.values():
    if v%k == 0:
        result += v//k
    else:
        result += v//k + 1
    
print(result)