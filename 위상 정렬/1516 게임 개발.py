import sys
from collections import defaultdict, deque
input = sys.stdin.readline

layer, time = defaultdict(list), defaultdict(int)

# 건물의 종류 수 n
n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)


for node in range(1, n + 1):
    row = list(map(int, input().split()))
    time[node] = row[0]
    row = row[1:-1]
    
    for prev_node in row:
        graph[prev_node].append(node)
        indegree[node] += 1
        

def solution():
    queue = deque()
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        result[node] += time[node]
        
        for next in graph[node]:
            indegree[next] -= 1
            result[next] = max(result[next], result[node])
            
            if not indegree[next]:
                queue.append(next)
                
    for i in range(1, n + 1):
        print(result[i])
                

solution()