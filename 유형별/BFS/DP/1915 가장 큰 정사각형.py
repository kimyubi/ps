import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []

# n x m의 0, 1로 된 배열에서 1로 된 가장 큰 정사각형의 크기를 구해라
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

ans = 0
for i in range(0, n):
    for j in range(0, m):
        if i > 0 and j > 0 and graph[i][j] != 0:
            graph[i][j] += min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) 
                
        ans = max(graph[i][j], ans)
                
print(ans ** ans)

