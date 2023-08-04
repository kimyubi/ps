import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

n, m = map(int, input().split())
# 치즈가 있는 부분 1, 치즈가 없는 부분 0
map = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    queue = deque()
    melting = []
    for i in range(n):
        for j in range(m):
            if map[i][j]:
                queue.append([i, j])
                
    while queue:
        x, y = queue.popleft()
        room_temperature = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 한 변이 실내 온도의 공기와 접촉
                if not map[nx][ny]:
                    room_temperature += 1
                    
        if 2 <= room_temperature:
            melting.append([x,y])
    
    for x in map:
        print(x)
    print() 
    for x, y in melting:
        map[x][y] = 0
             
    for x in map:
        print(x)
        
    print('========================================\n')
answer = 0
while 0 < sum([sum(x) for x in map]): 
    bfs()
    answer += 1
    
print(answer)

#<그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다.```