import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# n x m의 0, 1로 된 배열에서 1로 된 가장 큰 정사각형의 크기를 구해라
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def solution():
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                continue
            if graph[i][j] != 0:
                graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1
                
            ans = max(graph[i][j], ans)
                
    return ans * ans


print(solution())