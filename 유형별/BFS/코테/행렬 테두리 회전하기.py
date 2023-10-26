def solution(rows, columns, queries):
    answer = []
    matrix = [[(((i-1) * columns) + j) for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    
    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
        tmp = matrix[r1][c1]
        min_number = tmp
        
        # 왼쪽 세로
        for i in range(r1, r2):
            matrix[i][c1] = matrix[i+1][c1]
            min_number = min(min_number, matrix[i][c1])
        
        # 아래쪽 가로
        for i in range(c1, c2):
            matrix[r2][i] = matrix[r2][i+1]
            min_number = min(min_number, matrix[r2][i])
            
        # 오른쪽 세로
        for i in range(r2, r1, -1):
            matrix[i][c2] = matrix[i-1][c2]
            min_number = min(min_number, matrix[i][c2])
            
        # 위쪽 가로
        for i in range(c2, c1 ,-1):
            matrix[r1][i] = matrix[r1][i-1]
            min_number = min(min_number, matrix[r1][i])
            
        matrix[r1][c1+1] = tmp
        answer.append(min_number)
                             
    return answer