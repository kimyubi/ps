import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)

for i in range(n) :
    card = int(input())
    dict[card] += 1

result = sorted(dict.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])