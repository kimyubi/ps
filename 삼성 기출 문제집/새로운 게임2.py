import sys
from collections import defaultdict
input = sys.stdin.readline

# 체스판의 크기 n, 말의 개수 k
n, k = map(int, input().split())

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 체스판의 정보 info / 0 : 흰색 / 1: 빨간색 / 2: 파란색
info = [list(map(int, input().split())) for _ in range(n)]
piece = defaultdict(list)
graph = [[[] for _ in range(n)] for _ in range(n)]

for idx in range(1, k + 1):
    x, y, d = map(int, input().split())
    piece[idx] = [x-1, y-1, d-1]
    graph[x-1][y-1].append(idx)
    
def change_direction(d):
    if d in (0, 2):
        return d + 1
    else:
        return d - 1
    
for i in range(1, 1001):
    for number in range(1, k + 1):
        x, y, d = piece[number]
        idx = graph[x][y].index(number)
    
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or info[nx][ny] == 2:
            d = change_direction(d)
            nx, ny = x + dx[d], y + dy[d]
            piece[number][2] = d
            
            if not (0 <= nx < n and 0 <= ny < n) or info[nx][ny] == 2:
                continue
        
        if not info[nx][ny]:
            graph[nx][ny].extend(graph[x][y][idx:])
            
            if 4 <= len(graph[nx][ny]):
                print(i)
                sys.exit(0)
                
            for item in graph[x][y][idx:]:
                piece[item][0], piece[item][1] = nx, ny
                
            del graph[x][y][idx:]      
            
        elif info[nx][ny] == 1:
            graph[nx][ny].extend(graph[x][y][idx:][::-1])
            
            if 4 <= len(graph[nx][ny]):
                print(i)
                sys.exit(0)
            
            for item in graph[x][y][idx:][::-1]:
                piece[item][0], piece[item][1] = nx, ny
                
            del graph[x][y][idx:]
            
print(-1)
            
            
            
        
        
        
    