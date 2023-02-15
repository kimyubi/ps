import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x_list = list(map(int, input().split()))


for x in x_list:
    print(1 if binary_search(array, x, 0, n-1) else 0)
