import sys

input = sys.stdin.readline

# 삼각형의 크기 n
n = int(input())
t = [input().split() for _ in range(n)]

k = 2
for i in range(1, n):
    for j in range(k):
        # 맨 왼쪽이면
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        
        # 맨 오른쪽이면
        elif i == j:
            t[i][j] = t[i-1][j-1] + t[i][j]
            
        else:
            t[i][j] = max(t[i-1][j],t[i-1][j-1] ) + t[i][j]
            
    k += 1
    
print(max(t[n-1]))
            