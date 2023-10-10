import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

# 정점의 개수 n, 간선의 개수 e 
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
# 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1, v2
v1, v2 = map(int, input().split())

# 1 - v1 - v2 - n
# 1 - v2 - v1 - n
def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if distance[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
                
    return distance


result1_v1, resultv1_v2, resultv2_n = dijkstra(1)[v1], dijkstra(v1)[v2], dijkstra(v2)[n]
result1_v2, resultv1_n = dijkstra(1)[v2], dijkstra(v1)[n]

if INF in(result1_v1, resultv1_v2, resultv2_n) and INF in(result1_v2, resultv1_v2, resultv1_n):
    print(-1)
    
else:
    print(min(result1_v1 +  resultv1_v2 +  resultv2_n, result1_v2 +  resultv1_v2 +  resultv1_n))