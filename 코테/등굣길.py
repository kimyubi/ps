def solution(m, n, puddles):
    answer = 0
    
    # 집의 좌표를 1로 초기화
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    
    # 웅덩이의 좌표를 -1로 초기화
    for puddle in puddles:
        map[puddle[1]-1][puddle[0]-1] = -1
    
    for i in range(n):
        for j in range(m):
            # 현재 위치가 집이거나 웅덩이면 좌표 값을 갱신하지 않는다.
            if (i == 0 and j == 0) or map[i][j] == -1:
                continue
            
            # 첫번째 행
            if i-1 < 0:
                # 바로 왼쪽 칸이 웅덩이이면
                if map[i][j-1] == -1:
                    map[i][j] = 0
                else:
                    map[i][j] = map[i][j-1]
                        
            # 첫번째 열
            elif j-1 < 0:
                # 바로 위쪽 칸이 웅덩이이면
                if map[i-1][j] == -1:
                    map[i][j] = 0
                else:
                    map[i][j] = map[i-1][j]
            
            else:
                if -1 not in (map[i-1][j], map[i][j-1]):
                    map[i][j] = map[i-1][j] + map[i][j-1]
                else:
                    map[i][j] = max(0, map[i-1][j]) + max(0, map[i][j-1])
   
    return map[-1][-1] % 1000000007