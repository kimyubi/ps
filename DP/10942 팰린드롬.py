import sys
input = sys.stdin.readline

# 자연수 n
n = int(input())
numbers = list(map(int, input().split()))

# 질문의 개수 m
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    s, e = q[i]
    tmp = numbers[s-1:e]
    
    print(1 if tmp == tmp[::-1] else 0)