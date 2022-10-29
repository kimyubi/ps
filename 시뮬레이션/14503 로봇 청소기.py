# 18시 33분 시작
from dbm import ndbm
import sys
from collections import deque

input = sys.stdin.readline

# 세로 크기 n, 가로 크기 m
n,m = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표 (r,c), 바라보는 방향 d
# d = 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)
r,c,d = map(int, input().split())

# 빈 칸은 0, 벽은 1
graph = [list(map(int, input().split())) for _ in range(n)] 
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

visited[r][c] = True
ans = 1

while True:
    flag = False
    
    for _ in range(4):
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                r, c = nx, ny
                flag = True
                ans += 1
                break
            
        
    if flag == False:
        bx, by = r-dx[d], c-dy[d]
        if graph[bx][by] == 1:
            print(ans)
            break
        else:
            r, c = bx, by
            
        