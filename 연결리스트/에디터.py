from collections import deque
import sys

input = sys.stdin.readline

x = input().rstrip()

m = int(input())

left = deque(x)
right = deque()

for _ in range(m):
    s = list(input().rstrip().replace(" ", ""))
    
    if s[0] == 'L':
        if len(left) != 0:
            right.appendleft(left.pop())
            
    
    elif s[0] == 'D':
        if len(right) != 0:
            left.append(right.popleft())
            
    
    elif s[0] == 'B':
        if len(left) != 0:
            left.pop()
    
    else:
        c = s[1]
        left.append(c)
        

print(''.join(left) + ''.join(right))