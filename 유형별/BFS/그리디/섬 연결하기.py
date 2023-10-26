# 크루스칼 알고리즘 이용
# 가중치를 오름차순으로 정렬하여 가중치가 작은 것부터 선택하는 그리디 알고리즘

def solution(n, costs):
    answer = 0
    
    # 비용을 오름차순으로 정렬
    costs.sort(key = lambda x: x[2]) 
    link = set([costs[0][0]])
    
    while len(link) < n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:
                continue
            
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])
                answer += cost[2]
                break
            
    return answer