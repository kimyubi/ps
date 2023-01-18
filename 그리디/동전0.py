import sys

n, k = map(int, input().split())

a = [int(input()) for _ in range(n)]
cnt = 0

for coin in reversed(a):
    cnt += k // coin
    k = k % coin
    
print(cnt)