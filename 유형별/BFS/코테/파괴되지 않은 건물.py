def solution(board, skills):
    answer = 0
    
    for skill in skills:
        skill_type, r1, c1, r2, c2, degree = skill
        
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if skill_type == 1:
                    board[i][j] -= degree
                    continue
                else:
                    board[i][j] += degree
                    continue
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if 0 < board[i][j]:
                answer += 1
    
    return answer