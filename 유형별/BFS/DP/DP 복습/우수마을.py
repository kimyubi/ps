import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# n개의 마을
n = int(input())

# citizens : 마을 주민 수 
citizens = [0] + list(map(int, input().split()))

edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
    

# dp[i] : [정점 i가 우수 마을이 아닌 경우 우수 마을 주민 수의 총합, 우수 마을인 경우 우수 마을 주민 수의 총합]
dp = [[0, x] for x in citizens]
visited = [False for _ in range(n + 1)]

def dfs(root_node):
    visited[root_node] = True
    
    for next in edge[root_node]:
        if not visited[next]:
            dfs(next)
            
            dp[root_node][1] += dp[next][0]
            dp[root_node][0] += max(dp[next][0], dp[next][1])

dfs(1)   
print(max(dp[1]))
