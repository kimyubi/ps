import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def topology_sort(n, graph, rank, indegree):
    print(graph, indegree)
    result = []
    queue = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(rank[i])
            
    if not queue:
        print("IMPOSSIBLE")
        return
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for next in graph[rank[node]]:
            indegree[rank[next]] -= 1
            
            if not indegree[rank[next]]:
                queue.append(rank[next])
                
    
    print(result)
    return 
    

for t in range(int(input())):
    # 팀의 수 n
    n = int(input())
    data = [0]  + list(map(int, input().split()))
    rank = defaultdict(int)
    for i in range(1, n + 1):
        rank[data[i]] = i
        
    
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(1, n):
        graph[i].extend(data[i+1 : ])
        indegree[i + 1] = i
    
    # 상대적인 등수가 바뀐 쌍의 수 m
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[rank[a]]:
            graph[rank[a]].remove(b)
            indegree[rank[b]] -= 1
            
            graph[rank[b]].append(a)
            indegree[rank[a]] += 1
            
        else:
            graph[rank[b]].remove(a)
            indegree[rank[a]] -= 1
            
            graph[rank[a]].append(b)
            indegree[rank[b]] += 1
    
    topology_sort(n, graph, rank, indegree)      
    
            