import sys

input = sys.stdin.readline

# 테스트 케이스의 개수
t = int(input())

# 수열 p
p = [0] * 101
p[1], p[2], p[3] = 1, 1, 1

for i in range(4, 101):
    p[i] = p[i-3] + p[i-2]


for _ in range(t):
    n = int(input())
    print(p[n])