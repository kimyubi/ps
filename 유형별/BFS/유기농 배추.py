from collections import deque

# 테스트 케이스의 개수 T
T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y,farm,visited,M,N,K):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if farm[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

def execution():  
    #  배추밭의 가로길이 M,  배추밭의 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    M, N, K = map(int, input().split())
    farm = [list([0] * M) for _ in range(N)]
    visited = [list([False] * M) for _ in range(N)]


    for _ in range(K):
        i,j = map(int, input().split())
        farm[j][i] = 1              
        cnt = 0
        
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i,j,farm,visited,M,N,K)
        
        
    print(cnt)

for _ in range(T):
    execution()
    
