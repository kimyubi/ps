import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return 
        
    for i in numbers:
        if len(s) == 0 or s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()
           
dfs() 

        