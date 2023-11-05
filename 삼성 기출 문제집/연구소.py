import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline


# 지도의 세로 크기 n, 지도의 가로 크기 m
n, m = map(int, input().split())
# 0 : 빈 칸, 1 : 벽, 2 : 바이러스
graph = [list(map(int, input().split())) for _ in range(n)] 


empty_wall_positions = []
virus_positions = []
    
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            empty_wall_positions.append([i, j])
                
        if graph[i][j] == 2:
            virus_positions.append([i, j])

candidates = combinations(empty_wall_positions, 3)    

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def spread_virus(copy_graph):
    queue = deque(deepcopy(virus_positions))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not copy_graph[nx][ny]:
                    copy_graph[nx][ny] = 2
                    queue.append([nx, ny])
    
    size = 0
    for row in copy_graph:
        size += row.count(0)
    
    return size
                    


def solution():
    answer = 0
    
    for candidate in candidates:
        copy_graph = deepcopy(graph)
       
        # 벽 세우기
        for i, j in candidate:
            copy_graph[i][j] = 1
       
        # 바이러스 퍼뜨리고, 안전 영역의 최대 크기 구하기 
        answer = max(answer, spread_virus(copy_graph))
        
    return answer
    
print(solution())