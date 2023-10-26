import sys
input = sys.stdin.readline

INF = int(1e9)

# 도시의 개수 n
n = int(input())

# 버스의 개수 m
m = int(input())
graph = [[] for _ in range(n + 1)]


dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dist[i][j] = 0
            
for _ in range(m):
    # 시작 도시 a, 도착 도시 b, 필요한 비용 c
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != INF else 0 , end=' ')
    print()