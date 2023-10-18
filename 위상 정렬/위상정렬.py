from collections import deque

# 노드의 개수 v, 간선의 개수 e
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
# 위상 정렬 함수
def topology_sort():
    result = []
    queue = deque()
    
    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    # 큐가 빌때까지 반복
    while queue:
        node = queue.popleft()
        result.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            
            if indegree[next] == 0:
                queue.append(next)
                
    print(*result)
    

topology_sort()