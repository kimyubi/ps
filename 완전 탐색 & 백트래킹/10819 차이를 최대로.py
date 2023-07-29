import sys
from itertools import permutations
input = sys.stdin.readline

# 배열의 길이인 n의 최댓값이 8로 매우 작으므로 순열 활용
n = int(input())
arr = list(map(int, input().split()))
answer = 10 **6 *(-1)

for x in permutations(arr, n):
    tmp = 0
    for i in range(n-1, 0, -1):
        tmp += abs(x[i] - x[i-1])
    answer = max(tmp, answer)
        
print(answer)