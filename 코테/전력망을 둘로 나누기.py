from collections import defaultdict, deque
import sys
def split_network(dic,n):
    visited = [False for _ in range(n+1)]
    visited[1] = True
    queue = deque([1])
    
    while queue:
        x = queue.popleft()
        for next in dic[x]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    
    return abs(visited.count(False)-1 - visited.count(True))
                
                
def solution(n, wires):
    answer = sys.maxsize
    dic = defaultdict(deque)
    
    for a, b in wires:
        dic[a].append(b)
        dic[b].append(a)
    
    keys = sorted(dic, key= lambda x: -len(dic[x]))
    
    for key in keys:
        adj = dic[key]
    
        for i in range(len(adj)):
            x = dic[key].popleft()
            answer = min(answer,split_network(dic,n))
            if answer == 0:
                return 0
            dic[key].append(x)
    return answer