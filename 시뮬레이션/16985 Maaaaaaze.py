from itertools import permutations
import sys
from collections import deque

input = sys.stdin.readline

# 0은 참가자가 들어갈 수 없는 칸, 1은 들어갈 수 있는 칸
boards = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
tmp = []

result = sys.maxsize

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

# 배열의 90도 회전
def rotate(b):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4 - i] = b[i][j];

    return tmp

#  참가자는 판 5개를 쌓는데, 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있다. 
def solution():
    global tmp 
    for x in permutations(boards):
        tmp = list(x)
        dfs(0)


# 이 함수가 이해가 안된다.
def dfs(depth):
    global tmp
    
    if depth == 5:
        # 출구가 들어갈 수 있는 칸이라면
        if tmp[4][4][4]:
            bfs(tmp)
        return

    for i in range(4):
        # 입구가 들어갈 수 있는 칸이라면
        if tmp[0][0][0]:
            dfs(depth+1)
        
        tmp[depth] = rotate(tmp[depth]) 
            
  
def bfs(b):
    global result
    q = deque([(0,0,0)])
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]

    while q:
        h, y, x = q.popleft()
        if (h, y, x) == (4, 4, 4):
            result = min(result, dist[4][4][4])
            if result == 12: # 가장 짧은 경로의 경우 출력 후 종료
                print(result)
                exit()
            return

        for i in range(6):
            nh = h + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nh < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if b[nh][ny][nx] == 1 and dist[nh][ny][nx] == 0:
                    q.append((nh, ny, nx))
                    dist[nh][ny][nx] = dist[h][y][x] + 1
                    
            
            
            
solution()

if result == sys.maxsize:
    result = -1
print(result)