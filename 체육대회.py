# 4:19 백트래킹
answer = 0
def solution(ability):
    # 학생 수,   종목 수
    num_of_student, num_of_event = len(ability), len(ability[0])
    visited = [False] * num_of_student
    
    def dfs(depth, sum, visited):
        global answer
        if depth == num_of_event:
            answer = max(answer, sum)
            return
            
        for i in range(num_of_student):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, sum + ability[i][depth], visited)
                visited[i] = False
    
    dfs(0, 0, visited)
    return answer