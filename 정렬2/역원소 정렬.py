import sys

input = sys.stdin.readline
x = list(map(int, input().split()))

n = x[0]
l = []
cnt = 0

while True:
    if cnt == 0:
        x = x[1::]
    
    for k in x:
        tmp = str(k)[::-1]        
        while tmp[0] == '0':
            tmp = tmp[1::]
            
        
        l.append(int(tmp))
    
    if len(l) == n:
        break
    
    x = list(map(int, input().split()))
    cnt += 1
    
        
l.sort()
for x in l:
    print(int(x))