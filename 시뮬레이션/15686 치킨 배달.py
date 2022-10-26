from itertools import combinations
from sys import maxsize

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


graphs = []
houses, chickens = [], []

ans = maxsize

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i,j))
            
        elif graph[i][j] == 2:
            chickens.append([i,j])
            
            
            
for comb in combinations(chickens, m):
    temp = 0
    
    for house in houses:
        dist = maxsize
        for i in range(m):
            dist = min(dist, abs(house[0] - comb[i][0]) + abs(house[1] - comb[i][1]))
        temp += dist
    
    ans = min(ans, temp)     
    

print(ans)