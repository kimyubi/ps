import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산

n = int(input())
m = int(input())

indegree = [0] * (n + 1)
graph = defaultdict(list)

def topology_sort(graph, indegree):
    basic_components = []
    mid_componets = defaultdict(defaultdict)
    
    queue = deque()
    
    for i in range(1, n + 1):
        # 진입 차수가 0인 부품은 기본 부품이다.
        if not indegree[i]:
            queue.append(i)
            basic_components.append(i)

    while queue:
        node = queue.popleft()
        
        for next_component, cnt in graph[node]:
            if indegree[next_component]:
                # 재료가 되는 부품이 기본 부품인 경우
                if node in basic_components:
                    mid_componets[next_component][node] = cnt  
                    
                # 재료가 되는 부품이 중간 부품인 경우
                else:
                    for key in mid_componets[node].keys():
                        if key not in mid_componets[next_component]:
                            mid_componets[next_component][key] = 0
                            
                        mid_componets[next_component][key] += (mid_componets[node][key] * cnt)
                
            indegree[next_component] -= 1
            
            if not indegree[next_component]:
                queue.append(next_component)
    
    # 완제품 n을 만드는데 필요한 기본 부품의 개수를 출력
    for idx in basic_components:
        print(idx, mid_componets[n][idx])
    
        
for _ in range(m):
    # 중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다
    x, y, k = map(int, input().split())
    graph[y].append([x, k])
    indegree[x] += 1
    
topology_sort(graph, indegree)

    
