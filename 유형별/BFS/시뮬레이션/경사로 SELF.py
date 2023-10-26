import sys

input = sys.stdin.readline

# 지도의 크기 n, 경사로의 길이 l
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def line_check(line):
    for i in range(1,n):
        
        # 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
        if abs(line[i] - line[i-1]) > 1:
            return False
        
        # 경사로는 낮은 칸에 놓는다.
        if line[i] < line[i-1]:
            for j in range(l):
                if i+j >= n or line[i] != line[i+j] or slope[i+j]:
                    return False
                
                if line[i] == line[i+j]:
                    slope[i+j] = True
                    
                    
        elif line[i-1] < line[i]:
            for j in range(l):
                if i-1-j < 0 or line[i-1] != line[i-1-j] or slope[i-1-j]:
                    return False
                
                if line[i-1] == line[i-1-j]:
                    slope[i-1-j] = True
        
    return True
    
ans = 0

for i in range(n):
    slope = [False] * n
    if line_check([graph[i][j] for j in range(n)]):
        ans += 1
        
for j in range(n):
    slope = [False] * n
    if line_check([graph[i][j] for i in range(n)]):
        ans += 1
        
        
print(ans)