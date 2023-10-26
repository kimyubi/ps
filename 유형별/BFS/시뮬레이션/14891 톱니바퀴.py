import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

# 4개의 톱니바퀴의 상태를 저장한다.
gears = [[0]] + [list(map(int,list(input().rstrip()))) for _ in range(4)]

# 회전 횟수 k
k = int(input())

# 회전 방법
# [회전 시킨 톱니바퀴의 번호, 방향]
# 방향: 1 -> 시계 방향, -1 -> 반시계 방향
rotation_method = [list(map(int,input().split())) for _ in range(k)]

# 톱니바퀴를 시계방향으로 회전시키는 함수
def turn_clockwise(num):
    global gears
    gear = deque(gears[num])
    
    # gear의 마지막 요소를 pop 하여 맨 앞에 삽입한다.
    x = gear.pop()
    gear.appendleft(x)
    
    gears[num] = gear
    
# 톱니바퀴를 반시계방향으로 회전시키는 함수
def turn_counterclockwise(num):
    global gears
    gear = deque(gears[num])
    
    # gear의 맨 앞 요소를 pop하여 맨 뒤에 삽입한다.
    x = gear.popleft()
    gear.append(x)
    
    gears[num] = gear
    

# rotate(회전 시킨 톱니바퀴의 번호, 방향)
def rotate(num, direction, visited):
    origin_gear = deepcopy(gears[num])
    
    # 시계 방향 회전
    if direction == 1:
        turn_clockwise(num)
    
    # 반시계 방향 회전
    else:
        turn_counterclockwise(num)
    
    visited[num] = True
    
    # 회전 시킨 톱니바퀴가 맨 왼쪽 톱니바퀴인 경우
    if num == 1:
        if origin_gear[2] == gears[2][6]:
            return
        else:
            if not visited[2]:
                rotate(2, -direction, visited)
    
    # 회전 시킨 톱니바퀴가 맨 오른쪽 톱니바퀴인 경우
    elif num == 4:
        if origin_gear[6] == gears[3][2]:
            return
        else:
            if not visited[3]:
                rotate(3,-direction, visited)
        
    # 회전 시킨 톱니바퀴의 양쪽에 톱니바퀴가 있는 경우
    else:
        if origin_gear[6] != gears[num-1][2] and not visited[num-1]:
            rotate(num-1, -direction, visited)
            
        if origin_gear[2] != gears[num+1][6] and not visited[num+1]:
            rotate(num+1, -direction, visited)
        
    

def solution():
    ans = 0
    
    for num, direction in rotation_method:
        
        # 한번의 톱니바퀴 회전에서 이미 방문했던(회전했던) 톱니바퀴는 다시 회전시키지 않는다.
        visited = [False] * 5
        rotate(num, direction, visited)
        
    # n극은 0, s극은 1
    # 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    if gears[1][0] == 1:
        ans += 1

    # 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    if gears[2][0] == 1:
        ans += 2
           
    # 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    if gears[3][0] == 1:
        ans += 4
        
    # 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
    if gears[4][0] == 1:
        ans += 8
    
    return ans
    
print(solution())