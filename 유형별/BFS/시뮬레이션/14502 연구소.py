import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도의 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())

# 지도의 모양
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 바이러스가 있는 위치 저장
def set_vireses():
    viruses = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                viruses.append((i,j))
    
    return viruses

candidates = []

def set_candidates():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                candidates.append((i,j))
    


def bfs():
    global ans
    
    copy_graph = deepcopy(graph)
    viruses = set_vireses()
    
    while viruses:
        x, y = viruses.popleft()
        
        for i in range(4):
            nx, ny = x+ dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if copy_graph[nx][ny] == 0:
                    copy_graph[nx][ny] = 2
                    viruses.append((nx, ny))
    
    tmp = 0
    for g in copy_graph:
        tmp += g.count(0)
    
    ans = max(tmp, ans)
        


def solution():
    global graph 
    
    for candidate in combinations(candidates,3):
        for i in range(3):
            x, y = candidate[i][0], candidate[i][1]
            graph[x][y] = 1
        
        bfs()
        
        for i in range(3):
            x, y = candidate[i][0], candidate[i][1]
            graph[x][y] = 0
        
        


set_candidates()             
solution()
print(ans)