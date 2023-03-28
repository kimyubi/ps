from collections import deque
def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
        
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    queue = deque([1])
    
    while queue:
        x = queue.popleft()
        for next in adj[x]:
            if not visited[next]:
                visited[next] = visited[x] + 1
                queue.append(next)
                
    return visited.count(max(visited))