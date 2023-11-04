from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for com in combinations(cards, 3):
    card_sum = sum(com)
    
    if card_sum <= m:
        answer = max(answer, card_sum)
        
        if answer == m:
            break
        
print(answer)