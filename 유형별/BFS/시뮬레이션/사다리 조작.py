
# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

# 단, 두 가로선이 연속하거나 서로 접하면 안 된다
def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)