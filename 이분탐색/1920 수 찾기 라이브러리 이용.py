import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def binary_search(array, target):
    left_index = bisect_left(array, target)
    right_index = bisect_right(array, target)
    
    if right_index > left_index:
        print(1)
    else:
        print(0)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x_list = list(map(int, input().split()))


for x in x_list:
    binary_search(array, x)
