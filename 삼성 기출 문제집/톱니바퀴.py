import sys
from collections import deque
input = sys.stdin.readline

# 톱니바퀴의 상태, 0 : N극 / 1 : S극
gears = [list(map(int,list(input().rstrip()))) for _ in range(4)]

def rotate(idx, gear, direction):
    global gears
    gear = deque(gear)

    if direction == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())
    gears[idx] = gear
     
def dfs(idx, direction):
    if not 0 <= idx < 4:
        return
    
    left_side, right_side = gears[idx][-2], gears[idx][2]
    if not visited[idx]:
        rotate(idx, gears[idx], direction)
        visited[idx] = True
        
    if 0 <= idx -1 < 4 and gears[idx -1][2] != left_side and not visited[idx-1]:
        dfs(idx -1, -direction)
        
    if 0 <= idx + 1 < 4 and gears[idx + 1][-2] != right_side and not visited[idx + 1]:
        dfs(idx + 1, -direction) 
    
for _ in range(int(input())):
    # direction =>  1 : 시계 방향, -1 : 반시계 방향
    idx, direction = map(int, input().split())
    idx -= 1
    visited = [False] * 4
    dfs(idx, direction)
     
answer = 0     
for i in range(4):
    s_score = 2 ** i
    if gears[i][0] == 1:
        answer += s_score
        
print(answer)
       
    