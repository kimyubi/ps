import sys
input = sys.stdin.readline
# https://www.acmicpc.net/problem/11660


# 표의 크기 n, 합을 구해야 하는 횟수 m
n, m = map(int, input().split())

graph = [[0] * (n + 1)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        graph[i][j] += graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2]-graph[x2][y1-1]-graph[x1-1][y2]+graph[x1-1][y1-1])