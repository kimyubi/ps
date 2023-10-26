import sys
import heapq
input = sys.stdin.readline

# 카드의 개수 n, 카드 합체 횟수 m
n, m = map(int, input().split())

card = list(map(int, input().split()))
heapq.heapify(card)

for _ in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    
    heapq.heappush(card, a+b)
    heapq.heappush(card, a+b)

    
print(sum(card))
