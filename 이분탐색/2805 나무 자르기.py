import sys

input = sys.stdin.readline

# 나무의 수 n, 집으로 가져가려고 하는 나무의 길이 m
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start, end = 0, trees[-1]

while start <= end:
    mid = (start + end) // 2
    total = 0

    for tree in trees:
        if tree >= mid:
            total += tree - mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)