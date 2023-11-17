import sys
input = sys.stdin.readline

def solution():
    global answer 
    
    # 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
    # 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
    pointer = -1
    
    while 0 < m:
        # 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
        pointer += 1
        
        if pointer == c:
            break
        
        # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
        # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
        for idx in range(r):
            if board[idx][pointer]:
                answer += board[idx][pointer].pop()[-1]
                break
            
        sharks = []
        for i in range(r):
            for j in range(c):
                if board[i][j] and board[i][j][0]:
                    sharks.append([board[i][j][0], (i, j)])
                        
        while sharks:
            shark, position = sharks.pop()
            s, d, z = shark
            x, y = position
            
            # 초기 x,y 좌표와 방향
            fx, fy = x, y
            fd = d
            cnt = 0
                
            while True:
                if cnt == s:
                    board[fx][fy].remove([s, fd, z])
                    board[x][y].append([s, d, z])
                    break
                    
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    cnt += 1
                    x, y = nx, ny
                        
                else:
                    if d == 1 or d == 3:
                        d += 1
                    else:
                        d -= 1
        
        # 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
        for i in range(r):
            for j in range(c):
                if board[i][j] and 2 <= len(board[i][j]):
                    board[i][j].sort(key=lambda x: x[-1])
                    del board[i][j][:-1]
                
                 

if __name__ == '__main__':
    # 위, 아래, 오른쪽, 왼쪽
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]

    # 격자판의 크기 r * c, 상어의 수 m
    r, c, m = map(int, input().split())
    board = [[list() for _ in range(c)] for _ in range(r)]
    
    for _ in range(m):
        x, y, s, d, z = map(int, input().split())
        board[x-1][y-1].append([s, d, z])
 

    answer = 0
    solution()
    print(answer)