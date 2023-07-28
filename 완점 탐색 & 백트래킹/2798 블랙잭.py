import sys
from itertools import combinations
input = sys.stdin.readline

# 카드의 개수 n, 숫자 m
n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for com in combinations(cards, 3):
    card_sum = sum(com)
    if card_sum <= m:
        answer = max(answer, card_sum)
    
print(answer)