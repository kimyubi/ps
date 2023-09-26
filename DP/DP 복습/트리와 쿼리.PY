import sys
input = sys.stdin.readline

# 정점의 수 n, 루트의 번호 r, 쿼리의 수 q
n, r, q = map(int, input().split())
edge = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
    
query = [int(input()) for _ in range(q)]

# dp[i] : 정점 i를 루트로 하는 서브트리에 속한 정점의 수
dp = [1 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(root_node):
    visited[root_node] = True
    
    for next in edge[root_node]:
        if not visited[next]:
            dfs(next)
            
            dp[root_node] += dp[next]
        

dfs(r)

for q in query:
    print(dp[q])