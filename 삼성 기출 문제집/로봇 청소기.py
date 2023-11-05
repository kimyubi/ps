# 8:27 ~ 8:48

import sys
input = sys.stdin.readline

# 북 / 동 / 남 / 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방의 세로 크기 n과 가로 크기 m
n, m  = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표 r, c / 처음에 로봇 청소기가 바라보는 방향 d
r, c, d = map(int, input().split())

# 0 : 청소되지 않은 빈칸, 1: 벽, 청소된 칸 : 2 /  테두리는 모두 벽이다.
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not graph[r][c]:
        graph[r][c] = 2
        answer += 1
        
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는지 확인한다.
    exist_not_clean_room = False
    
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < m:
            if not graph[nr][nc]:
                exist_not_clean_room = True
                
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not exist_not_clean_room:
        nr, nc = r - dx[d], c - dy[d]
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if 0 <= nr < n and 0 <= nc < m:
            # 다음 칸이 벽이 아니면 한 칸 후진한다.
            if graph[nr][nc] != 1:
                r, c = nr, nc 
                continue
            
            # 다음 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
            
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반 시계 방향으로 90도 회전한다.
        d = (d + 3) % 4
        
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진한다.
        nr, nc = r + dx[d], c + dy[d]
        
        # 앞쪽 칸이 청소되지 않은 빈 칸이면 한 칸 전진한다.
        if not graph[nr][nc]:
            r, c = nr, nc
            continue 
                
print(answer)