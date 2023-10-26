import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

ans = 0 
for x, y in zip(a,b):
    ans += x * y

print(ans)