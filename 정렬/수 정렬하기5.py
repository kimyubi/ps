import sys

input = sys.stdin.readline
n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))

for x in sorted(values):
    print(x)

