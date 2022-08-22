seq = list(map(int,input().split()))


def dfs():
    global seq
    global s
    
    if len(s) == 6:
        print(*s)
        return
        
    for i in seq[1:]:
        if i not in s:
            if len(s) == 0 or s[-1] < i:
                
                s.append(i)
                dfs()
                s.pop()
            
    
    
while seq[0] != 0:
    s = []
    dfs()
    print()
    seq = list(map(int,input().split()))