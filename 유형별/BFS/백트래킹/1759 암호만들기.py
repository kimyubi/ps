l,c = map(int, input().split())
seq = input().split()
seq.sort()

s = []

def dfs():
    global s
    
    if len(s) == l:
        m, j = 0, 0
        
        for i in s:
            if i in ('a', 'e', 'i', 'o', 'u'):
                m += 1
            else:
                j += 1
                
        if m >= 1 and j >= 2:   
            print("".join(s))
        return
    
    for i in seq:
        if i not in s:
           if len(s) == 0 or s[-1] < i:
                s.append(i)
                dfs()
                s.pop()
                
dfs()