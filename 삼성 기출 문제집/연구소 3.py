import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

def bfs(data, visited, queue):
    next_queue = []
    remove_cnt = 0
                
    while queue:
        x, y = queue.pop()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] != 1 and not visited[nx][ny]:
                    if data[nx][ny] == 0:
                        remove_cnt += 1
                        
                    data[nx][ny] = 3
                    next_queue.append([nx, ny])
                    
    return data, visited, next_queue, remove_cnt


def spread_virus(data, comb, visited):
    data, visited, queue, remove_cnt = bfs(data, visited, comb)
    
    time = 0
    goal = zero_cnt
    
    while True:
        time += 1
        goal -= remove_cnt
            
        # 빈 칸에 바이러스를 모두 전파한 경우
        if not goal:
            return time
            
        # 더 이상 전파 시킬 수 없는 경우
        if not queue:
            return MAX_SIZE
        
        data, visited, queue, remove_cnt = bfs(data, visited, queue)
        

def solution():
    global answer
    for comb in combinations(inactive_virus, m):
        copy_data = deepcopy(data)
        visited = [[False] * n for _ in range(n)]
        for x, y in comb:
            copy_data[x][y] = 3
        answer = min(answer, spread_virus(copy_data, list(comb), visited))        
    

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
    zero_cnt = 0 
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                inactive_virus.append([i, j])
            elif data[i][j] == 0:
                zero_cnt += 1
                
    if not zero_cnt:
        print(0)
    else:     
        solution()
        print(answer if answer != MAX_SIZE else -1)