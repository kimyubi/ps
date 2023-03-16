import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

start = 0
end = 0

nums.sort()
result = sys.maxsize

while start <= end and end < n:
    sub = nums[end] - nums[start]
    if sub < m:
        end += 1
    
    else:
        result = min(sub, result)
        start += 1
    
print(result)
    
    