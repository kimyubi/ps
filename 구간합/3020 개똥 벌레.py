import sys
input = sys.stdin.readline

# 동굴의 길이 n, 높이 h
n, h = map(int, input().split())

# i번째 구간으로 날아갈때, 파괴해야하는 장애물의 수
obstacle = [0] * h

for i in range(n):
    v = int(input())
    
    # 종유석
    if i % 2 == 0:
        obstacle[h - v] += 1
        
    # 석순
    else:
        obstacle[0] += 1
        obstacle[v] -= 1
        
        
for i in range(1, n + 1):
    obstacle[i] += obstacle[i-1]

ans = min(obstacle)
print(ans, obstacle.count(ans), sep= ' ')