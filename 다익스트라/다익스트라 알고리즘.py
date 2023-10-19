import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 n, 간선의 개수 m
n, m = int(input().split())

# 시작 노드 start
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])
    
def dijkstra(start):
    queue = []
    
    # 시작 노드로 가기 위한 최단 거리를 0으로 설정하여, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[node] < dist:
            continue
        
        # 현재 노드와 인접한 노드들을 확인
        for next in graph[node]:
            cost = dist + next[1]
            
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))
                
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
    