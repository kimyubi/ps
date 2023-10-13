import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

# 나무 그루터기의 개수 n, 오솔길의 개수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d * 2))
    graph[b].append((a, d * 2))
    
dp_fox = [INF] * (n + 1)
def dijstra_fox(start):
    dp_fox[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap)
        if dp_fox[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < dp_fox[next_node]:
                dp_fox[next_node] = distance
                heapq.heappush(heap, (distance, next_node))
                
                
# dp[0][i] : i번째 노드까지 느리게 도착한 경우 최소 시간
# dp[1][i] : i번째 노드까지 빠르게 도착한 경우 최소 시간
dp_wolf = [[INF] * (n + 1) for _ in range(2)]

def dijstra_wolf(start):
    # 달빛 늑대는 출발할 때 오솔길 하나를 달빛 여우의 두 배의 속도로 달려간다.
    SPEED = False
    dp_wolf[SPEED][start] = 0
    heap = []
    heapq.heappush(heap, (0, start, SPEED))
    
    
    while heap:
        dist, node, SPEED = heapq.heappop(heap)
        if dp_wolf[SPEED][node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            # 현재 노드까지 빠르게 도착했다면, 다음 노드로 느리게 출발
            if SPEED:
                distance = dist + next_dist * 2
            else:
                # 현재 노드까지 느리게 도착했다면, 다음 노드로 빠르게 출발
                distance = dist + next_dist // 2
                
            if distance < dp_wolf[not SPEED][next_node]:
                dp_wolf[not SPEED][next_node] = distance
                heapq.heappush(heap, (distance, next_node, not SPEED))
      
                    
         
dijstra_fox(1)
dijstra_wolf(1)

result = 0
for i in range(1, n + 1):
    if dp_fox[i] < min(dp_wolf[0][i], dp_wolf[1][i]):
        result += 1

print(result)
        