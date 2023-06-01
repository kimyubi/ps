# 맨해튼 거리: 각 좌표의 차이(절대값)의 합
# P: 응시자가 앉아있는 자리, O: 빈 테이블, X: 파티션
from itertools import combinations
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(person1, person2, graph):
    visited = [[0] * 5 for _ in range(5)]
    
    r1, c1 = person1
    r2, c2 = person2
    
    queue = deque([(r1, c1)])
    while queue:
        x, y = queue.popleft()
        
        if x == r2 and y == c2:
            if visited[x][y] <= 2:
                return False
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    return True
    
def dedicate(graph):
    peoples = []
    
    # 응시자 좌표를 peoples 배열에 기록한다.    
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                peoples.append([i,j])
                    
    # 응시자 2명의 조합을 구한다.
    for person1, person2 in combinations(peoples, 2):
        r1, c1 = person1
        r2, c2 = person2
        
        # 맨해튼 거리가 2 이하이면
        if abs(r1-r2) + abs(c1-c2) <= 2:
            # 파티션을 고려했을 때, 맨해튼 거리가 2 이하이면, 그 응시자 조합은 거리두기를 지키지 않고 있는 것이다. 
            if not bfs(person1, person2, graph):
                return False
            
    return True
    
def solution(places):
    answer = []
    
    for place in places:
        graph = [list(line) for line in place]
        
        # 모든 응시자가 거리두기를 지키고 있는 경우
        if dedicate(graph):
            answer.append(1)
        # 한 명이라도 지키지 않고 있는 경우    
        else:
            answer.append(0)
         
    return answer