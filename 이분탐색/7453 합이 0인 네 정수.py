import sys

input = sys.stdin.readline

# 배열의 크기 n
n = int(input())
arr = [sum(list(map(int, input().split()))) for _ in range(n)]

print(arr)