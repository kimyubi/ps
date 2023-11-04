import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
members = {i for i in range(n)}
data = [list(map(int, input().split())) for _ in range(n)]


answer = 100
for start in combinations(members, n //2):
    start = set(start)
    link = members - start
    
    start_sum = 0
    link_sum = 0
    
    for i, j in combinations(start, 2):
        start_sum += data[i][j]
        start_sum += data[j][i]    
        
    for i, j in combinations(link, 2):
        link_sum += data[i][j]
        link_sum += data[j][i]    
        
    
    answer = min(answer, abs(start_sum - link_sum))
    
    
print(answer)