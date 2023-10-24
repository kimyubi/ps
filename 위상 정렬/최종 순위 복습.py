import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def topology_sort(indegree, graph, n):
    result = []
    queue = deque()
    
    for i in range(1, n + 1):
        if not indegree[i]:
            queue.append(i)

    if not queue:
        print("IMPOSSIBLE")
        return
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for next in graph[node]:
            indegree[next] -= 1
            
            if not indegree[next]:
                queue.append(next)
                
    if len(result) < n:
        print("IMPOSSIBLE")
        return
    else:
        print(*result)
        return
        



for _ in range(int(input())):
    # 팀의 수 n
    n = int(input())
    
    data = [0] + list(map(int, input().split()))
    rank = defaultdict(int)
    for i in range(1, n + 1):
        rank[i] = data[i]
        
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        indegree[rank[i]] = i - 1
        for j in range(i + 1, n + 1):
            graph[rank[i]].append(rank[j])
            
    
    # 상대적인 등수가 바뀐 쌍의 수 m
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            
            graph[a].append(b)
            indegree[b] += 1
            
        else:
            graph[a].remove(b)
            indegree[b] -= 1
            
            graph[b].append(a)
            indegree[a] += 1
            
    
    topology_sort(indegree, graph, n)
            
    