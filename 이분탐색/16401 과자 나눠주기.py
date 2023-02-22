import sys

input = sys.stdin.readline

# 조카의 수 m, 과자의 수 n
m, n = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort()
dedicate = []

def solve(start, end, target):
    global dedicate
    if start > end:
        return
    
    mid = (start + end) // 2
    
    sum = 0
    for snack in snacks:
        sum += snack // mid
        
    if sum < target:
        return solve(start, mid-1, target)
    
    else:
        dedicate.append(mid)
        return solve(mid+1, end, target)
        
    
solve(1, snacks[-1] , m)
print(dedicate[-1] if len(dedicate) != 0 else 0)
