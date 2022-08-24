# 테케 1번 통과 못함

from collections import deque

def solution(tickets):
    tickets = list(tickets)
    visited = [False] * (len(tickets))
    
    answer = []
    queue = deque()
    
    tickets.sort()
    for i, ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            answer.append(ticket[0])
            answer.append(ticket[1])
            
            queue.append(ticket)
            visited[i] = True
            break
        
    
    while queue:
        pre = queue.popleft()
        
        for i, ticket in enumerate(tickets):
            if pre[1] == ticket[0] and not visited[i]:
                print(ticket)
                visited[i] = True
                
                answer.append(ticket[1])
                queue.append(ticket)
    
    return answer
    


print(solution( [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
