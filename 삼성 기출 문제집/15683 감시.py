# 10:47 ~
import sys
from copy import deepcopy
input = sys.stdin.readline

# 북, 남, 서, 동
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

directions = {
    1: [[1], [2], [3], [4]],
    2: [[1, 2], [3, 4]],
    3: [[1, 4], [2, 4], [2, 3], [1, 3]],
    4: [[1, 3, 4], [1, 2, 4], [2, 3, 4], [1, 2, 3]],
    5: [[1, 2, 3, 4]]
}


# 사무실의 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())
# 0 : 빈칸, 1 ~ 5: cctv
data = [list(map(int, input().split())) for _ in range(n)]

cctv_position = []
for i in range(n):
    for j in range(m):
        if 1 <= data[i][j] <= 5:
            cctv_position.append([i, j, data[i][j]])
cctv_cnt = len(cctv_position)      
 
answer = sys.maxsize
def spread(x, y, direction, copy_data):
    tmp_x, tmp_y = x, y
    
    for d in direction:
        while True:
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                break
            
            if copy_data[nx][ny] == 6:
                break
            
            if not copy_data[nx][ny]:
                copy_data[nx][ny] = '#'
            
            x, y = nx, ny
        x, y = tmp_x ,tmp_y
        
    return copy_data
        

def dfs(depth, data: list):
    global answer
    
    if depth == cctv_cnt:
        cnt = 0
        for row in data:
            cnt += row.count(0)
        answer = min(answer, cnt)
        return
    
    x, y, number = cctv_position[depth]
    for direction in directions[number]:
        dfs(depth + 1, spread(x, y, direction, deepcopy(data)))

dfs(0, data)
print(answer)
        
        