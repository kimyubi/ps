import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 :  n, 간선의 개수 :  m
n, m = map(int, input().split())

# 시작 노드 : start
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range (n + 1)]

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i].append([j,c])
    
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            cost = dist + node[1]
            
            if cost < distance[node[0]]:
                dist[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))
            
    
