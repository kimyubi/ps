import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도의 크기 n
n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)

num = []
count, result = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            DFS(i, j)
            num.append(count)
            result += 1
            count = 0
            
print(result)

num.sort()
print(*num, sep='\n')