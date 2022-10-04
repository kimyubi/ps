import sys

input = sys.stdin.readline
n = int(input())
l = []

for _ in range(n):
    x = list(input().split())
    
    l.append([int(x[1]), int(x[2]), int(x[3]), x[0]])


l.sort(key = lambda x : (-x[0], x[1], -x[2], x[3]))

for x in l:
    print(x[3])
    
    