import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 트리의 정점 개수 n
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
info = [[0,1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(node):
    visited[node] = True
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
        
            # 자신이 얼리어답터가 아닌 경우, 자식들은 반드시 모두 얼리어답터여야 한다.
            info[node][0] += info[next][1]
            # 자신이 얼리어답터인 경우, 자식은 뭐든 상관없으니 얼리어답터가 최소인 경우를 선택한다.
            info[node][1] += min(info[next])
    
dfs(1)
print(min(info[1]))