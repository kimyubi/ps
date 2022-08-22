import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()

s = []
is_used = [False for _ in range(n)]

def dfs():
    pre = 0
    
    if len(s) == m:
        print(' '.join(map(str,s)))
        return 
  
    for i, x in enumerate(numbers):   
        if not is_used[i] and pre != x:
            s.append(x)
            is_used[i] = True
            pre = x
            
            dfs()
            s.pop()
            is_used[i] = False     
        
            
           
dfs() 

        