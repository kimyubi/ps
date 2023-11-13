import sys
input = sys.stdin.readline

# 세로 선의 개수 N, 가로 선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수
N, M, H = map(int, input().split())
ladder = [[0] * (N + 1) for _ in range(H + 1)]
answer = 4


for _ in range(M):
    # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.
    a, b = map(int, input().split())
    ladder[a][b] = 1
     
def check():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if ladder[j][now - 1]:
                now -= 1
            elif ladder[j][now]:
                now += 1
                
        if i != now:
            return False
    return True

candidates = []
for i in range(1, H + 1):
    for j in range(1, N):
        if 1 not in (ladder[i][j-1], ladder[i][j], ladder[i][j+1]):
            candidates.append([i, j])
            
def dfs(depth, idx):
    global answer, ladder
    
    if 3 < depth or answer <= depth:
        return
    
    if check():
        answer = min(answer, depth)
        return 
    
    for i in range(idx, len(candidates)):
        x, y = candidates[i]
        if 1 not in (ladder[x][y-1], ladder[x][y+1]):
            ladder[x][y] = 1
            dfs(depth + 1, i + 1)
            ladder[x][y] = 0
            
dfs(0,0)
print(answer if answer < 4 else -1)
    