import sys
from itertools import combinations

input = sys.stdin.readline

# N * N 도시, 최대 M개의 치킨 집
N, M = map(int, input().split())

# 0 : 빈칸, 1 : 집, 2 : 치킨 집
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []
# 치킨 집, 집 좌표 구하기
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i,j])
        if city[i][j] == 2:
            chickens.append([i, j])
            
answer = sys.maxsize

for comb in combinations(chickens, M):
    city_chicken_dist = 0
    
    for hx, hy in houses:
        chicken_dist = sys.maxsize
        for cx, cy in comb:
            chicken_dist = min(chicken_dist, abs(hx-cx) + abs(hy-cy))
        city_chicken_dist += chicken_dist
        
    answer = min(answer, city_chicken_dist)    
print(answer)
                
        