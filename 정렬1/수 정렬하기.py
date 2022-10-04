import sys

input = sys.stdin.readline
n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))
    
values.sort()

for x in values:
    print(x)

