def dfs(n,computers,start,visited):
    visited[start] = True
    
    for connect in range(n):
        if start != connect and computers[start][connect] == 1:
            if not visited[connect]:
                dfs(n,computers,connect,visited)


# 연결된 노드를 모두 탐색하고 빠져나오면 그것이 하나의 네트워크
def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for start in range(n):
        if not visited[start]:
            dfs(n,computers,start,visited)
            answer += 1
            
    return answer
            
    
    
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))