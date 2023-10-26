import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def is_exist(num):
    left = bisect_left(cards, num)
    right = bisect_right(cards, num)
    
    if left != right:
        return True
    return False

# 숫자 카드의 개수 n
n = int(input())

# 숫자 카드에 적혀있는 정수 cards
cards = list(map(int, input().split()))
cards.sort()

# 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 m개의 정수 nums
m = int(input())
nums =  list(map(int, input().split()))


for num in nums:
    if is_exist(num):
        print(1, end=' ')
    else:
        print(0, end=' ')
        
        


