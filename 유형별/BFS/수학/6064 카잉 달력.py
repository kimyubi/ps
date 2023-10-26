import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    
    _x, _y = 1, 1
    
    calendar = [[_x, _y]]
    while True:
        if _x == m and _y == n:
            break
        
        if _x < m:
            _x += 1
        else:
            _x = 1
            
        if _y < n:
            _y += 1
        else:
            _y = 1
            
        calendar.append([_x,_y])
    
    
    if [x,y] in calendar:
        print(calendar.index([x,y]) + 1)
    else:
        print(-1)