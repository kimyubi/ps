# 10: 56 ~
import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def change_dir(d):
    return (d + 1) % 8

graph = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(0, len(data), 2):
        num, direction = data[j], data[j + 1]
        graph[i][j//2] = [num, direction - 1]
        
def find_fish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j
    return False

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(graph, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(graph, i)
        if position:
            x, y = position
            d = graph[x][y][1]

            for _ in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    # 상어가 있는 자리가 아니면
                    if not (nx == now_x and ny == now_y):
                        graph[x][y][1] = d
                        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                        break
                    
                d = change_dir(d)
    return graph
                    
def get_possible_positions(graph, now_x, now_y, d):
    positions = []

    for _ in range(4):
        now_x += dx[d]
        now_y += dy[d]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if graph[now_x][now_y][0] != -1:
                positions.append([now_x, now_y])
    return positions


answer = 0
# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(graph, now_x, now_y, total):
    global answer
    graph = deepcopy(graph) # 리스트를 통째로 복사
    
    total += graph[now_x][now_y][0] # 현재 위치의 물고기 먹기
    graph[now_x][now_y][0] = -1 # 물고기를 먹었으므로 번호 값을 -1로 변환
    
    graph = move_all_fishes(graph, now_x, now_y) # 전체 물고기 이동 시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(graph, now_x, now_y, graph[now_x][now_y][1])
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if not positions:
        answer = max(answer, total) # 최댓값 저장
        return 
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(graph, next_x, next_y, total)

# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(graph, 0, 0, 0)
print(answer)