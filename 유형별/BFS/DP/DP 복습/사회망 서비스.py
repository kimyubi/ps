import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

# 정점 개수 n
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# dp = [내가 ea가 아닐 때 최소 ea 수, 내가 ea일때 최소 ea 수]
dp = [[0, 1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(node):
    visited[node] = True
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
            
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][0], dp[next][1])
            
dfs(1)
print(min(dp[1]))
    
    
