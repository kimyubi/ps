
def w_move(idx, x, y, nx, ny):
    global graph
    graph[nx][ny].append(graph[x][y][idx:])
    del graph[x][y][idx:]

def r_move(idx, x, y, nx, ny):
    global graph
    graph[nx][ny].append(graph[x][y][idx:][::-1])
    del graph[x][y][idx:]

def b_move(dx, dy, idx, x, y, d, number):
    global piece
    nx, ny = x + dx[d], y + dy[d]
         # 체스판을 벗어나는 경우에는 이동하지 않고 가만히 있는다.
    if not (0 <= nx < n and 0 <= ny < n):
        piece[number][2] = d
            
        # 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
    elif info[nx][ny] == 2:
        piece[number][2] = d
            
        # A번 말의 이동 방향을 반대로 하고 한 칸 이동한다
    else:
        if not info[nx][ny]:
            w_move(idx, x, y, nx, ny)
                # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
        elif info[nx][ny] == 1:
            r_move(idx, x, y, nx, ny)
            

def piece_move():
    for number in range(1, k + 1):
        x, y, d = piece.get(number)
        idx = graph[x][y].index(number)
    
        nx, ny = x + dx[d], dy[d]
        if 0 <= nx < n and 0 <= ny < n:
        # 이동하려는 칸이 흰색인 경우
            if not info[nx][ny]:
            # a번 말의 위에 다른 말이 있는 경우에는 a번 말과 위에 있는 모든 말이 이동한다.
                w_move(idx, x, y, nx, ny)
            
        # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            elif info[nx][ny] == 1:
                r_move(graph, idx, x, y, nx, ny)
        
        # 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
        # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
            else:
            # 이동 방향을 반대로
                if d in (0, 2):
                    d += 1
                else:
                    d -= 1
                b_move(dx, dy, idx, x, y, d, number)

        else:
        # 이동 방향을 반대로
                if d in (0, 2):
                    d += 1
                else:
                    d -= 1
                b_move(dx, dy, idx, x, y, d, number)

answer = -1
for x in range(1, 1000):
    piece_move()
    
    for i in range(n):
        for j in range(n):
            if 4 <= len(graph[i][j]):
                answer = x
                break


print(answer)
            