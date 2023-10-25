import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산

n = int(input())
m = int(input())

indegree = [0] * (n + 1)
graph = defaultdict(list)

def topology_sort(graph, indegree):
    result = defaultdict(int)

    mid_componets = defaultdict(defaultdict)
    queue = deque()
    
    for i in range(1, n + 1):
        # 진입 차수가 0인 노드는 기본 부품이다.
        if not indegree[i]:
            queue.append(i)
            result[i] += 1


    while queue:
        node = queue.popleft()
        for next_component, cnt in graph[node]:
            if indegree[next_component]:
                if node in result.keys():
                    mid_componets[next_component][node] = cnt  
                    
                else:
                    # node : 5, key = (1, 2), next_component: 6
                    for key in mid_componets[node].keys():
                        if not key in mid_componets[next_component]:
                            mid_componets[next_component][key] = 0
                            
                        mid_componets[next_component][key] += (mid_componets[node][key] * cnt)
                
            indegree[next_component] -= 1
            
            if not indegree[next_component]:
                queue.append(next_component)
    
    base_components = sorted(result.keys())
    for c in base_components:
        print(c, mid_componets[n][c])
    
        
for _ in range(m):
    # 중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다
    x, y, k = map(int, input().split())
    graph[y].append([x, k])
    indegree[x] += 1

topology_sort(graph, indegree)

    
