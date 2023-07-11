# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는다.
def gain_score(m, n, board):
    success_index = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != 'X' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                if [i,j] not in success_index:
                    success_index.append([i,j])
                if [i+1,j] not in success_index:
                    success_index.append([i+1,j])
                if [i,j+1] not in success_index:
                    success_index.append([i,j+1])
                if [i+1,j+1] not in success_index:
                    success_index.append([i+1,j+1])
                    
    for i, j in success_index:
        board[i][j] = 'X'
    return len(success_index), board

# 판의 높이 m, 폭 n
def compact(m, n, board):
    for i in range(n):
        x, position = 'X', m - 1
        for j in range(m-1, -1, -1):
            if board[j][i] == 'X':
                continue
            if x == 'X':
                x = board[j][i]
            else:
                board[position][i] = x
                x = board[j][i]
                position -= 1
                
            board[j][i] = 'X'
            
        if x != 'X':
            board[position][i] = x     
                
        
    return board

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