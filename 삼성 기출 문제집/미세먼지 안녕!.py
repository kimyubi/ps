# 10:32 ~ 12:30
import sys
input = sys.stdin.readline

answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# (r, c): r행 c열, t : t초가 지난 후 구사과의 방에 남아있는 미세먼지의 양 출력 
r, c, t = map(int, input().split())

# 미세먼지의 양 amount
# -1은 공기청정기가 설치된 곳
dust_amount = [list(map(int, input().split())) for _ in range(r)]

cleaner_idx = 0
for idx in range(r):
    if dust_amount[idx][0] == -1:
        cleaner_idx = idx
        break
        
cleaner_up, cleaner_down = (cleaner_idx, 0), (cleaner_idx + 1, 0)

for _ in range(t):
    # 미세먼지 확산
    spread_list = []
    
    for i in range(r):
        for j in range(c):
            # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
            if 0 < dust_amount[i][j]:
                spread_list.append([i, j, dust_amount[i][j]])
    
    command = []
    for x, y, dust in spread_list:
        cnt = 0
        spread_amount = int(dust / 5)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and dust_amount[nx][ny] != -1:
                command.append([nx, ny, spread_amount])
                cnt += 1
                
        dust_amount[x][y] -= spread_amount * cnt 

    for x, y, d in command:
        dust_amount[x][y] += d
        
    # 아래쪽 공기 청정기 작동
    px, py = cleaner_down
    prev = 0
    d = 1
    while True:        
        if d == 2 and px == cleaner_down[0] and py == cleaner_down[1]:
            break
        
        if d == 1 and py == c - 1:
            d = 3
            
        elif d == 3 and px == r - 1:
            d = 0
            
        elif d == 0 and py == 0:
            d = 2
            
        nx, ny = px + dx[d], py + dy[d]
        tmp = dust_amount[nx][ny]
        dust_amount[nx][ny] = prev
        prev = tmp
            
        px, py = nx, ny
            
    dust_amount[cleaner_down[0]][cleaner_down[1]] = -1
    
            
    # 위쪽 공기 청정기 작동
    px, py = cleaner_up
    prev = 0
    d = 1
    while True:      
        if d == 3 and px == cleaner_up[0] and py == cleaner_up[1]:
            break
          
        if d == 1 and py == c - 1:
            d = 2
            
        elif d == 2 and px == 0:
            d = 0
            
        elif d == 0 and py == 0:
            d = 3
            
        nx, ny = px + dx[d], py + dy[d]
        tmp = dust_amount[nx][ny]
        dust_amount[nx][ny] = prev
        prev = tmp    
        px, py = nx, ny
            
    dust_amount[cleaner_up[0]][cleaner_up[1]] = -1
 
            
for i in range(r):
    for j in range(c):
        if 0 < dust_amount[i][j]:
            answer += dust_amount[i][j]
            


print(answer)
    
