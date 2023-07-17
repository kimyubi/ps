def solution(board, skill):
    answer = 0
    MAX_R, MAX_C = len(board), len(board[0])
    # 누적합 리스트
    cumulative_sum = [[0] * (MAX_C + 1) for _ in range(MAX_R + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        degree = -1 * degree if type == 1 else degree
        
        # 누적합 리스트 초기화
        cumulative_sum[r1][c1] += degree
        cumulative_sum[r2+1][c2+1] += degree
        cumulative_sum[r1][c2+1] -= degree
        cumulative_sum[r2+1][c1] -= degree
    
    # 행 기준 누적합
    for r in range(MAX_R + 1):
        for c in range(1, MAX_C + 1):
            cumulative_sum[r][c] += cumulative_sum[r][c-1]
            
    # 열 기준 누적합
    for c in range(MAX_C + 1):
        for r in range(1, MAX_R + 1):
            cumulative_sum[r][c] += cumulative_sum[r-1][c]
        
    return sum([1 if 0 < board[r][c] + cumulative_sum[r][c] else 0 for r in range(MAX_R) for c in range(MAX_C)])
