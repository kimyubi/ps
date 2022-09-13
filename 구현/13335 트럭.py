from collections import deque

# 트럭의 수, 다리의 길이, 다리의 최대 하중
n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridges = [0] * w
bridges = deque(bridges)

time = 0
while bridges:
    time += 1
    bridges.popleft()
    
    if trucks:
        if sum(bridges) + trucks[0] <= l:
            bridges.append(trucks.popleft())
        
        else:
            bridges.append(0)

print(time)