import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

answer = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
candidate = [[i, j] for j in range(m) for i in range(n) if not map[i][j]]
virus = [[i, j] for j in range(m) for i in range(n) if map[i][j] == 2]

def bfs(map_copy):
    queue = deque(deepcopy(virus))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < n and 0 <= ny < m:
                # 빈 칸이면 바이러스 퍼뜨리기
                if not map_copy[nx][ny]:
                    map_copy[nx][ny] = 2
                    queue.append([nx, ny])
    
    
    tmp = 0
    for x in map_copy:
        tmp += x.count(0)
    return tmp

for comb in combinations(candidate, 3):
    map_copy = deepcopy(map)
    for i, j in comb:
        map_copy[i][j] = 1
    
    answer = max(answer, bfs(map_copy))    
    
print(answer)