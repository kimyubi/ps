import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n_a, n_b = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

def find_x(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    
    if left_index == right_index:
        return False
    else:
        return True
    

ans = []
for x in a:
    if not find_x(b, x):
        ans.append(x)

n = len(ans)        
print(n)

if n != 0:
    ans.sort()
    print(*ans)
        