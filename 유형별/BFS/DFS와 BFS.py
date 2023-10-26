from collections import deque
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())    
    graph[x].append(y)
    graph[y].append(x)
    
    graph[x].sort()
    graph[y].sort()
    
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(graph, visited_dfs, V):
    visited_dfs[V] = True
    
    print(V, end= ' ')
    
    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(graph,visited_dfs,i)
        

def bfs(graph, visited_bfs, V):
    visited_bfs[V] = True
    queue = deque([V])
    
    while queue:
        item = queue.popleft()
        print(item, end=' ')
        
        for i in graph[item]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


dfs(graph,visited_dfs,V)
print()
bfs(graph,visited_bfs,V)
    
