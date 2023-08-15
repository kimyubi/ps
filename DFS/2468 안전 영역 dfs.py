import sys
from copy import deepcopy
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
MAX_HEIGHT = 0
ans = 0

for i in range(n):
    for j in range(n):
        MAX_HEIGHT = max(MAX_HEIGHT, graph[i][j])
        
def dfs(x, y, num, copy_graph):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    if num < copy_graph[x][y]:
        copy_graph[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny, num, copy_graph)
         
    
for num in range(0, MAX_HEIGHT + 2):
    cnt = 0
    
    copy_graph = deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if num < copy_graph[i][j]:
                dfs(i, j, num, copy_graph)
                cnt += 1
                
    ans = max(ans, cnt)
print(ans)            