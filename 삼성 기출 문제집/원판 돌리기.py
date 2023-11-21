# 11:27~ 1:03 
import sys
from collections import deque
input = sys.stdin.readline

# 반지름의 최대 크기 n: 1, 2 ... n / m : 원판에 적혀있는 정수의 개수 / t : 회전 수 
n, m, t = map(int, input().split())

# data[i][j] = i번째 원판에 적힌 j번째 수
data = [list(map(int, input().split())) for _ in range(n)]
    
def rotate(disk, direction, cnt):
    disk = deque(disk)
    for _ in range(cnt):
        # 시계 방향
        if not direction:
            disk.appendleft(disk.pop())
        # 반시계 방향
        else:
            disk.append(disk.popleft())
    return list(disk)
            
def calculate_remove_list():
    remove_list = []
    
    for i in range(n):
        for j in range(m):
            standard = data[i][j]
            if standard:
                if data[i][j-1] == standard and [i, j-1] not in remove_list:
                    remove_list.append([i, j-1])
                if data[i][(j+1)%m] == standard and [i, (j+1)%m] not in remove_list:
                    remove_list.append([i, (j+1)%m])
                    
                if i == 0:
                    if data[i+1][j] == standard and [i+1, j] not in remove_list:
                        remove_list.append([i + 1, j])
                elif i == n-1:
                    if data[i-1][j] == standard and [i-1, j] not in remove_list:
                        remove_list.append([i - 1, j])
                else:
                    if data[i+1][j] == standard and [i+1, j] not in remove_list:
                        remove_list.append([i + 1, j])
                    if data[i-1][j] == standard and [i-1, j] not in remove_list:
                        remove_list.append([i - 1, j])
    return remove_list

for _ in range(t):
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다.
    x, d, k = map(int, input().split())
    
    for number in range(1, n + 1):
        if number % x == 0:
            data[number-1] = rotate(data[number-1], d, k)
        
    # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
    remove_list = calculate_remove_list()
    if remove_list:
        for x, y in remove_list:
            data[x][y] = 0
            
    if not remove_list:
        total, cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if data[i][j]:
                    total += data[i][j]
                    cnt += 1
        if not cnt:
            break
        
        avg = total / cnt
        for i in range(n):
            for j in range(m):
                if data[i][j]:
                    if data[i][j] < avg:
                        data[i][j] += 1
                    elif avg < data[i][j]:
                        data[i][j] -= 1
 
answer = 0    
for disk in data:
    answer += sum(disk)
print(answer)