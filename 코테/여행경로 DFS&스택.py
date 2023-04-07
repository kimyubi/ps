from collections import defaultdict
def solution(tickets):
    # 출발지를 key, 도착지를 value로 하는 딕셔너리, dic 생성
    dic = defaultdict(list)
    
    for start, end in tickets:
        dic[start].append(end)
    
    # 도착지를 알파벳 순으로 정렬 => dic의 value를 정렬
    for key in dic:
        dic[key].sort()
        
    stack, path = ["ICN"], []
    
    def dfs():
        while len(stack) > 0:
            top = stack[-1]
        
            # top을 출발지로 하는 항공권이 없거나 이미 다 써버린 경우, 경로에 추가
            if top not in dic or not dic[top]:
                path.append(stack.pop())
            else:
                stack.append(dic[top].pop(0))
    
        return path[::-1]
    
    return dfs()