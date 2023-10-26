# dist 고르는게 잘못됐다..! 낼 다시 풀기
from collections import deque
def solution(n, weak, dist):
    friend_num = len(dist)
    dist.sort()
    dist = deque(dist)
    
    weak = [-1 * (n - x) if n/2 < x else x for x in weak]
    weak.sort()
    weak = deque(weak)
    
    while dist:
        if not weak:
            return friend_num - len(dist)
        
        friend = dist.pop()
        start, end = weak.popleft(), 0
        
        for idx, value in enumerate(weak):
            if friend < value - start:
                break
            end += 1
            
        for _ in range(end):
            weak.popleft()
        
    return -1



def bfs(map_copy, visited):
    for x in map_copy:
        print(x)
        
    return 0 

def spread_virus(map_copy):
    queue = deque(deepcopy(virus))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 빈 칸이면 바이러스가 퍼져나갈 수 있다.
                if map_copy[nx][ny] != 1:
                    map_copy[nx][ny] = 2
                    queue.append([nx, ny])
                    
    return map_copy
    
    
    
for comb in combinations(candidate, 3):
    map_copy = deepcopy(map)
    visited = [[False] * m for _ in range(n)]
    
    for i, j in comb:
        map_copy[i][j] = 1
        
    # 바이러스 퍼뜨리기
    map_copy = spread_virus(map_copy)
    
    answer = max(answer, bfs(map_copy, visited))    