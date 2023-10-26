import sys
input = sys.stdin.readline

# 수열의 길이 n
n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
total_sum = 0
result = sys.maxsize

while True:
    if total_sum >= s:
        result = min(end - start , result)
        
        total_sum -= nums[start]
        start += 1
        
    elif end == n:
        break
    
    else:
        total_sum += nums[end]
        end += 1
        

if result == sys.maxsize:
    print(0)
else:
    print(result)    
        
    
    