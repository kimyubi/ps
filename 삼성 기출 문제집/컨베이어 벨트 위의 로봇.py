# 12:14 ~
import sys
from collections import deque
input = sys.stdin.readline

# 컨베이어 벨트의 길이 n, 내구도가 0인 칸인 개수가 k개 이상이라면 종료한다.
n, k = map(int, input().split())

# 각 칸의 내구도 durability[i]
durability = deque(map(int, input().split()))

# 올리는 위치 0, 내리는 위치 (n - 1)
belt = deque([False for _ in range(2 * n)])

START, END = 0, (n - 1)

stage = 0
while True:
    stage += 1
    
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    durability.rotate(1)
    belt.rotate(1)
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 
    belt[END] = False
    
    for now in range(n-2, -1, -1):
        next = now + 1
        if belt[now] and not belt[next] and durability[next]:
            belt[now], belt[next] = False, True
            durability[next] -= 1
            
    belt[END] = False
    if durability[START]:
        belt[START] = True
        durability[START] -= 1
        
    if k <= durability.count(0):
        break
    
print(stage)
    
    
        
    
   