import sys

input = sys.stdin.readline

# 지도의 크기 n, 경사로의 길이 n
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def check_line(line):
    for i in range(1, n):
        
        # 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
        if abs(line[i] - line[i - 1]) > 1:
            return False
        
        if line[i] < line[i - 1]:
            for j in range(l):
                
                # 경사로를 놓다가 범위를 벗어나는 경우 / 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않는 경우 / 경사로를 놓은 곳에 또 경사로를 놓는 경우
                if i + j >= n or line[i] != line[i + j] or slope[i + j]:
                    return False
                
                if line[i] == line[i + j]:
                    slope[i + j] = True
                    
                    
        elif line[i] > line[i - 1]:
            for j in range(l):
                
                # 경사로를 놓다가 범위를 벗어나는 경우 / 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않는 경우 / 경사로를 놓은 곳에 또 경사로를 놓는 경우
                if i - 1 - j < 0 or line[i - 1] != line[i - 1 - j] or slope[i - 1 - j]:
                    return False
                
                if line[i - 1] == line[i - 1 - j]:
                    slope[i - 1 - j] = True
                    
    return True


for i in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for i in range(n)]):
        ans += 1

print(ans)