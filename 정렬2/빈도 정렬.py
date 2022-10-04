import sys
from collections import defaultdict
input = sys.stdin.readline
dict = defaultdict(list)

n, c = map(int, input().split())
inputs = list(map(int, input().split()))

for i, x in enumerate(inputs):
    if len(dict[x]) == 0:
        dict[x] = [i, 1]
    
    else:
        dict[x][1] += 1
        


result = [[i,j] for i,j in dict.items()]
result.sort(key=lambda x: (-x[1][1], x[1][0]))

ans = []
for i, j in result:
    ans += [i] * j[1]
        
print(*ans)

