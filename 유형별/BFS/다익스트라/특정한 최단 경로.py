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

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)