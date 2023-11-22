import sys
from copy import deepcopy

input = sys.stdin.readline

from collections import defaultdict
# 0: 시작점, 21: 도착점

# root1
graph = defaultdict(list)
for i in range(0, 21):
    graph[i].append(i + 1)

# root2
graph[5].append(22)
for i in range(22, 25):
    graph[i].append(i + 1)

# root 3    
graph[10].append(26)
graph[26].append(27)
graph[27].append(25)

# root 4
graph[15].append(28)
graph[28].append(29)
graph[29].append(30)
graph[30].append(25)

# root5
graph[25].append(31)
graph[31].append(32)
graph[32].append(20)

graph[21].append(21)
score = [0, 2, 4, 6, 8, 
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 
         30, 32, 34, 36, 38, 
         40, 0, 13, 16, 29, 
         25, 22, 24, 28, 27,
         26, 30, 35]

dice = list(map(int, input().split()))
destination = 21

answer = 0
def dfs(depth, total, pieces):
    global answer
    
    if depth == 10:
        answer = max(answer, total)
        return
    
    for i in range(4):
        now = pieces[i]
        
        # 현재 말의 위치가 파란색 칸 위인 경우
        if len(graph[now]) == 2:
            next = graph[now][1]
        else:
            next = graph[now][0]
            
        
        for _ in range(1, dice[depth]):
            next = graph[next][0]
            
        if next == destination or (next not in pieces):
            copy_pieces = deepcopy(pieces)
            copy_pieces[i] = next
            dfs(depth + 1, total + score[next], copy_pieces)
            

dfs(0, 0, [0, 0, 0, 0])
print(answer)
            

        