def solution(info, edges):
    answer = []
    SHEEP = 0
    visited = [False] * len(info)
    
    def dfs(sheep, wolf):
        if wolf < sheep:
            answer.append(sheep)
        else:
            return
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                
                if info[child] == SHEEP:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
       
                visited[child] = False
            
    
    visited[0] = True
    dfs(1, 0)
    
    return max(answer)
