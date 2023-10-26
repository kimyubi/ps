# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는다.
def gain_score(m, n, board):
    success_index = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != '0' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                if [i,j] not in success_index:
                    success_index.append([i,j])
                if [i+1,j] not in success_index:
                    success_index.append([i+1,j])
                if [i,j+1] not in success_index:
                    success_index.append([i,j+1])
                if [i+1,j+1] not in success_index:
                    success_index.append([i+1,j+1])
                    
    for i, j in success_index:
        board[i][j] = '0'
        
    return len(success_index), board

# 판의 높이 m, 폭 n
def compact(m, n, board):
    re_board = [''] * m
    for i in range(n):
        column = ''.join([board[j][i] for j in range(m)]).replace("0","").zfill(m)
        
        for j in range(m):
            re_board[j] += column[j]
         
    return [list(row) for row in re_board]


def solution(m, n, board):
    answer = 0
    board = [list(row) for row in  board]
    
    while True:
        score, board = gain_score(m, n, board)
        if not score:
            return answer
        
        board = compact(m, n, board)
        answer += score
        
    return answer