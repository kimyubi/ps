import sys
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 종이의 세로 크기 n과 가로 크기 m
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m  for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maxValue = 0
def dfs(i, j, sum, depth):
    global maxValue
    
    if depth == 4:
        maxValue = max(sum, maxValue)
        return
    
    for d in range(4):
        ni, nj = i + dx[d], j + dy[d]
        
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, sum + paper[ni][nj], depth + 1)
            visited[ni][nj] = False
            

def exce(i, j):
    global maxValue
    for bundle in combinations([x for x in range(4)], 3):
        tmp = paper[i][j]
        
        for d in bundle:
            ni, nj = i + dx[d], j + dy[d]
            if not (0 <= ni < n and 0 <= nj < m):     
                tmp = 0 
                break
            
            tmp += paper[ni][nj]
            
        maxValue = max(tmp, maxValue)
                      
                
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = False
        exce(i, j)
        
        
print(maxValue)
        