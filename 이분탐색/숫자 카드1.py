import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 카드의 개수 n
n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
x_list = list(map(int, input().split()))

def count_x(x):
    left_index = bisect_left(cards, x)
    right_index = bisect_right(cards, x)
    
    if left_index == right_index:
        return 0
    else:
        return 1

for x in x_list:
    print(count_x(x), end= ' ')




