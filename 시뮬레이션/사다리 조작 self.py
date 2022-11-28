import sys

input = sys.stdin.readline

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
N, M, H = map(int,input().split())

# 가로선 정보 기록
# 가로선의 정보: a, b -> b번 세로선과 b+1 세로선을 a번 점선 위치에서 연결했다는 의미 
horizontal_line = [[False] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    horizontal_line[a][b] = True

# 결과값을 4로 초기화
ans = 4

    
# 모든 i번 세로선의 결과가 i번이 나오는지 체크하는 check 함수 정의
def check():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if horizontal_line[j][now-1]:
                now -= 1
                
            elif horizontal_line[j][now]:
                now += 1
                
        if now != i:
            return False
    
    return True
                        

# 가로선을 연결할 후보 위치 
candidates = []

for i in range(1,H+1):
    for j in range(1, N):
        if not horizontal_line[i][j-1] and not horizontal_line[i][j] and not horizontal_line[i][j+1]:
            candidates.append([i,j])


# 메인 로직을 담당하는 dfs 함수
def dfs(depth, idx):
    global ans
    
    if depth >= ans:
        return 
    
    if check():
        ans = depth
        return
    
    for i in range(idx, len(candidates)):
        x, y = candidates[i]
        
        if not horizontal_line[x][y-1] and not horizontal_line[x][y+1]:
            horizontal_line[x][y] = True
            dfs(depth + 1, i + 1)
            horizontal_line[x][y] = False
        

dfs(0,0)
print(ans if ans < 4 else -1)
