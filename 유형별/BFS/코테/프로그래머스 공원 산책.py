def solution(park, routes):
    answer = []
    
    # 공원의 가로 길이 W
    W = len(park[0])
    
    # 공원의 세로 길이 H
    H = len(park)
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                position_x = i
                position_y = j
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        is_accept = True
        tmp_x = position_x
        tmp_y = position_y
        
        for i in range(n):
            # 북쪽 이동
            if op == 'N':
                tmp_x -= 1
            # 남쪽 이동
            elif op == 'S':
                tmp_x += 1
            # 서쪽 이동
            elif op == 'W':
                tmp_y -= 1
            # 동쪽 이동
            else:
                tmp_y += 1
            
            
            if not(0 <= tmp_x < H) or not(0 <= tmp_y < W):
                is_accept = False
                break
            if park[tmp_x][tmp_y] == 'X':
                is_accept = False
                break
                    
        if is_accept:
            position_x = tmp_x
            position_y = tmp_y
        
            
    return [position_x, position_y]
        
        