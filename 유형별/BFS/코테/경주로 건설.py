from collections import deque
import sys
    # 북, 남 서, 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    def bfs():
        n = len(board)
    
        MAX_VALUE = sys.maxsize
        answer = MAX_VALUE
        visited = [[[MAX_VALUE] * n for _ in range(n)] for _ in range(4)]
        
        queue = deque()
        
        for z in range(4):
            visited[z][0][0] = 0
            
        if board[0][1] != 1:
            queue.append([0, 1, 100, 3])
            visited[3][0][1] = 100
            
        if board[1][0] != 1:
            queue.append([1, 0, 100, 1])
            visited[1][1][0] = 100
        
        while queue:
            x, y, cost, z = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if i == z:
                    ncost = cost + 100
                else:
                    ncost = cost + 600
                
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                    if ncost < visited[i][nx][ny]:
                        visited[i][nx][ny] = ncost
                        queue.append([nx, ny, ncost, i])
        
        for z in range(4):
            answer = min(answer, visited[z][n-1][n-1])
        return answer
    
    return bfs()