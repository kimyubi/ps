import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def spread_virus(data, comb):
    visited = [[False] * n for _ in range(n)]
    
    queue = deque()
    zero_cnt = global_zero_cnt
    
    for x, y in comb:
        data[x][y] = 3
        visited[x][y] = True
        queue.append([x, y, 0])
        
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] != 1 and not visited[nx][ny]:
                        if data[nx][ny] == 0:
                            zero_cnt -= 1
                            
                        if not zero_cnt:
                            return time + 1
                            
                        data[nx][ny] = 3
                        queue.append([nx, ny, time + 1])
                        visited[nx][ny] = True
    return MAX_SIZE

def solution():
    global answer
    for comb in combinations(inactive_virus, m):
        answer = min(answer, spread_virus(deepcopy(data), comb))        
    

if __name__ == '__main__':
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 연구소의 크기 n, 놓을 수 있는 바이러스의 개수 m
    n, m = map(int, input().split())
    
    # 0: 빈 칸, 1 : 벽, 2 : 비활성 바이러스의 위치, 3: 활성 바이러스의 위치
    data = [list(map(int, input().split())) for _ in range(n)]
    
    MAX_SIZE = sys.maxsize
    answer = MAX_SIZE
    
    inactive_virus = []
    global_zero_cnt = 0 
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                inactive_virus.append([i, j])
            elif data[i][j] == 0:
                global_zero_cnt += 1
                
    if not global_zero_cnt:
        print(0)
    else:     
        solution()
        print(answer if answer != MAX_SIZE else -1)