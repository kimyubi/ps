import sys
from itertools import combinations
input = sys.stdin.readline

# 도시의 크기 n, 치킨집 개수 m
n, m = map(int, input().split())

# 0 : 빈 칸, 1 : 집, 2 : 치킨 집
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        
        elif city[i][j] == 2:
            chickens.append([i, j])
            
answer = sys.maxsize
for comb in combinations(chickens, m):
    # 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
    city_chicken_distance = 0
    
    for house_x, house_y in houses:
        # 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
        min_chicken_distance = sys.maxsize
        for chicken_x, chicken_y in comb:
            min_chicken_distance = min(min_chicken_distance, abs(chicken_x - house_x) + abs(chicken_y - house_y))
            
        city_chicken_distance += min_chicken_distance
        
    answer = min(answer, city_chicken_distance)
    
print(answer)
            
            
            
            
            
    
            