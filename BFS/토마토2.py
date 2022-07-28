from collections import deque
import queue
import sys

input = sys.stdin.readline
M,N,H = map(int, input().split())

storage = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)]for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if storage[i][j][k] == 1:
                queue.append((i,j,k))
                
if len(queue) == 0:
    print(-1)
    sys.exit(0)
elif len(queue) == M * N * H:
    print(0)
    sys.exit(0)
                
def bfs():
    while queue:
        x,y,z = queue.popleft()
        visited[x][y][z] = True
    
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if storage[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                    visited[nx][ny][nz] == True 
                    storage[nx][ny][nz] = storage[x][y][z] + 1
                    queue.append((nx,ny,nz))
                    
bfs()


day = 0
for i in range(H):
    for j in range(N):
        if 0 in storage[i][j]:
            print(-1)
            sys.exit(0)
        for k in range(M):
            day = max(day,storage[i][j][k])

print(day-1)


