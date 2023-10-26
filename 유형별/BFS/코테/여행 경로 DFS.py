from collections import defaultdict
def solution(tickets):
    answer = []
    # 출발지를 key, 도착지를 value로 하는 딕셔너리, dic 생성
    dic = defaultdict(list)
    
    for start, end in tickets:
        dic[start].append(end)
    
    # 도착지를 알파벳 순으로 정렬 => dic의 value를 정렬
    for key in dic:
        dic[key].sort()
        
    N = len(tickets) + 1 
    
    def dfs(x, route):
        if len(route) == N:
            return route
        
        for idx, country in enumerate(dic[x]):
            dic[x].pop(idx)
            r = route[:]
            r.append(country)
            
            ret = dfs(country, r)
            if ret:
                return ret
            
            dic[x].insert(idx, country)
     
    
    return dfs("ICN", ["ICN"])        
            
        