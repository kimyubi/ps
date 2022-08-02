import sys
from collections import deque
input = sys.stdin.readline
text = [deque(input().rstrip()) for _ in range(5)]
result = ''

while not(len(text[0]) == 0 and len(text[1]) == 0 and len(text[2]) == 0 and len(text[3]) == 0 and len(text[4]) == 0 ):
    if len(text[0]) != 0:
        result += text[0].popleft()
    if len(text[1]) != 0:
        result += text[1].popleft()
    if len(text[2]) != 0:
        result += text[2].popleft()
    if len(text[3]) != 0:
        result += text[3].popleft()
    if len(text[4]) != 0:
        result += text[4].popleft()

print(result)