import sys, copy

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 종류에 따른 감시 방향
dirction = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2] ,[2,3], [3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}

# cctv 리스트
cctv = [] 

# cctv들의 위치를 cctv 리스트에 저장
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            
            # x좌표, y좌표, cctv 종류
            cctv.append([i,j,graph[i][j]])
            

ans = 1e9


print(ans)
            