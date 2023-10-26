from collections import deque
import sys
N = int(sys.stdin.readline())

cards = deque([i for i in range(1, N+1)])

while cards:
    if len(cards) == 1:
        print(*cards)
        break
    
    cards.popleft()
    cards.append(cards.popleft())
    
    