dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def rotation(puzzle):
    return [list(x) for x in zip(*puzzle[::-1])]

def empty_side(game_board, puzzle, i, j, n):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):            
            # 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안된다.
            if puzzle[x][y] == 1:
                for k in range(4):
                    nx, ny = x + i + dx[k], y + j + dy[k]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if game_board[nx][ny] != 1:
                        return True

    return False

def is_match(puzzle, game_board, n):
    r = len(puzzle)
    c = len(puzzle[0])
    
    # 퍼즐 놓기 시작점 i,j
    for i in range(n-r+1):
        for j in range(n-c+1):
            match = True
            for x in range(len(puzzle)):
                for y in range(len(puzzle[0])):
                    game_board[x+i][y+j] += puzzle[x][y]
                    if game_board[x+i][y+j] != 1:
                        match = False
            
            if empty_side(game_board, puzzle, i, j,n):
                match = False

            if match:
                return True
            else:
                for x in range(len(puzzle)):
                    for y in range(len(puzzle[0])):
                        game_board[x+i][y+j] -= puzzle[x][y]

    return False
                
                
    
def transform(position):
    min_r, max_r = 100 ,-1
    min_c, max_c = 100, -1
    for r, c in position:
        min_r = min(r, min_r)
        max_r = max(r, max_r)
        min_c = min(c, min_c)
        max_c = max(c, max_c)
        
    len_r = max_r - min_r + 1
    len_c = max_c - min_c + 1
    
    puzzle = [[0] * len_c for _ in range(len_r)]
    
    for r, c in position:
        puzzle[r-min_r][c-min_c] = 1
        
    return puzzle
    
    
def bfs(x, y, visited, table, n):
    queue = [(x, y)]
    visited[x][y] = 1
    puzzle = []
    
    while queue:
        x,y = queue.pop()
        puzzle.append([x, y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return puzzle
    
            
def solution(game_board, table):    
    answer = 0
    puzzles = []
    puzzle_len = []
    # table의 행 길이
    n = len(table)
    visited = [[0] * n for _ in range(n)]
    
    # 테이블에서 퍼즐 꺼내기
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                puzzle_location = bfs(i,j,visited,table,n)
                puzzles.append(transform(puzzle_location))
                puzzle_len.append(len(puzzle_location))
                    
    
    for idx, puzzle in enumerate(puzzles):
        for _ in range(4):
            puzzle = rotation(puzzle)
            if is_match(puzzle, game_board, n):
                answer += puzzle_len[idx]
                break
                
    return answer
        