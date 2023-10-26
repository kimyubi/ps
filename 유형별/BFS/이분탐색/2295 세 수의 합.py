import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
two_sum = set()

for i in range(n):
    for j in range(i, n):
        two_sum.add(array[i] + array[j])
    
two_sum = list(two_sum)
two_sum.sort()

array.sort(reverse=True)

def find(x):
    left_index = bisect_left(two_sum, x)
    right_index = bisect_right(two_sum, x)
    
    if left_index == right_index:
        return False
    
    return True
    

def solve():
    for i in range(n):
        for j in range(i+1, n):
            if find(array[i] - array[j]):
                return array[i]
            

print(solve())
                