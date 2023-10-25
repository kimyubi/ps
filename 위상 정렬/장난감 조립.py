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
        for next_componet, cnt in graph[node]:
            if indegree[next_componet]:
                mid_componets[next_componet][node] = cnt    
                    
            indegree[next_componet] -= 1
            
            if not indegree[next_componet]:
                queue.append(next_componet)
                
    
    for component in mid_componets.keys():
        for key in mid_componets[component].keys():
            if key in result.keys():
                result[key] += mid_componets[component][key]
                
            else:
                cnt = mid_componets[component][key]
                mid_componets[component].pop(key)
                for prev_key in mid_componets[key].keys():
                    mid_componets[component][prev_key] += (mid_componets[key][prev_key] * cnt)
                    result[prev_key] += mid_componets[component][prev_key]
    
        
for _ in range(m):
    # 중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다
    x, y, k = map(int, input().split())
    graph[y].append([x, k])
    indegree[x] += 1

topology_sort(graph, indegree)

    
