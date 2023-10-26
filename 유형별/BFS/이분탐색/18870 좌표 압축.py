import sys

input = sys.stdin.readline
n = int(input())

nums = list(map(int, input().rstrip().split()))
origin = nums
nums = list(set(nums))
nums.sort()

dic = dict()
for idx, x in enumerate(nums):
    dic[x] = idx
    
for x in origin:
    print(dic[x], end = ' ')
 