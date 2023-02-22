import sys

input = sys.stdin.readline

# 이미 가지고 있는 랜선의 개수 k, 필요한 랜선의 개수 n
k, n = map(int, input().split())

# 랜선 lines
lines = [int(input()) for _ in range(k)]
lines.sort()

dedicate = []

def find_max_length(start, end, target):
    global dedicate
    if start > end:
        return
    
    mid = (start + end) // 2
    
    sum = 0
    for line in lines:
        sum += line // mid
        
    if sum < target:
        return find_max_length(start, mid-1, target)
    
    else:
        dedicate.append(mid)
        return find_max_length(mid+1, end, target)
        
        

find_max_length(1, lines[-1], n)
print(dedicate[-1])



