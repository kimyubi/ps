import sys

input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]    
line.sort()

keep = [line[0]]
ans = 0
for i in range(1, n):
    if line[i][0] <= keep[-1][1] < line[i][1]:
        keep[-1][1] = line[i][1]
    
    elif keep[-1][1] < line[i][0]:
        x, y = keep.pop()
        ans += y-x
        keep.append([line[i][0], line[i][1]])
        

ans += keep[0][1] - keep[0][0]
print(ans)