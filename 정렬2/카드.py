from collections import defaultdict,Counter
import sys

input = sys.stdin.readline
dict = defaultdict(int)

n = int(input())

for i in range(n):
    x = int(input())
    dict[x] += 1
    
counter = Counter(dict)
common = counter.most_common()

max = common[0][1]
l = []

for x in common:
    if x[1] == max:
        l.append(x[0])
       
l.sort() 
print(l[0])


