import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
LIS = [[nums[i]] for i in range(n)]


for i in range(n):
    tmp = list()
    for j in range(i):
        if nums[j] < nums[i]:
            x = list(LIS[j][0][:])
            print(x)
            x.append(nums[i])
            tmp.append(x)
            
        print('tmp',tmp)
    ll = sorted(tmp, key=lambda x: -len(x))
    if ll:
        LIS[i] = [ll[0]]
        print(LIS)
   