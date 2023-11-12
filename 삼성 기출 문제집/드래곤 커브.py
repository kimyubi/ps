import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [[0] * 101 for _ in range(101)]

for i in range(n):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    
    move = [d]
    for _ in range(g):
        for i in range(len(move) -1, -1, -1):
            move.append((move[i] + 1) % 4)
        
    for i in move:
        x, y = x + dx[i], y + dy[i]
        board[x][y] = 1
            
result = 0
for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
                result += 1
                
print(result)