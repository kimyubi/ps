import sys

input = sys.stdin.readline

n = int(input())
l = []
tmp = []

for i in range(n):
    x = input().rstrip()
    
    if x in tmp:
        continue
    
    l.append([len(x), x])
    tmp.append(x)

l.sort(key=lambda x: (x[0], x[1]))

for x in l:
    print(x[1])