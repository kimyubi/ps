import sys
from bisect import bisect_left

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    ans = 0
    n, m = map(int, input().split())
    
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    b.sort()
    
    for i in a:
        ans += bisect_left(b,i)
    
    print(ans) 
                
    
    