import sys
from collections import deque

input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def solution():
    x, y = 1, 1
    time, dir = 0, 0

    board[x][y] = 1
    dq = deque([[x,y]])

    while True:
        time += 1

        x = x + dx[dir]
        y = y + dy[dir]
        

        if x < 1 or x > n or y < 1 or y > n or board[x][y] == 1: break

        if board[x][y] == 0:
            tail_x, tail_y = dq.popleft()
            board[tail_x][tail_y] = 0

        board[x][y] = 1
        dq.append([x, y]) 
        
        if time in times.keys():
            if times[time] == 'L':
                dir = (dir + 1) % 4
                
            else: dir = (dir + 3) % 4

    return time

# 빈 칸: 0, 뱀: 1, 사과: 2 
n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 2
    
l = int(input())

times = {}
for _ in range(l):
    t, d = input().split()
    times[int(t)] = d

# 메인 코드 부분
print(solution())