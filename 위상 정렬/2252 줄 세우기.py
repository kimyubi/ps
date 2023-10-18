import sys
from collections import deque
input = sys.stdin.readline

# 학생 수 n, 키를 비교한 횟수 m
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    queue = deque()
    
    for i in range(1, n + 1):
        if not indegree[i]:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for next in graph[node]:
            indegree[next] -= 1
            
            if not indegree[next]:
                queue.append(next)
                
    print(*result)
    
topology_sort()