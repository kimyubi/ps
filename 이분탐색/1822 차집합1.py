import sys

input = sys.stdin.readline

n_a, n_b = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = list(set(a) - set(b))
result.sort()
n = len(result)

print(n)
if n != 0:
    print(*result)