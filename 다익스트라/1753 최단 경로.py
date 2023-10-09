import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())

# 시작 정점의 번호 K
K = int(input())

# 가중치 dp
dp = [INF]*(V+1)

heap = []
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    heapq.heappush(heap,(0, start))
    dp[start] = 0

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei, next_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])