import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    arr[0][i] += arr[0][i-1]
    
for i in range(1, n):
    start_left = [arr[i-1][j] + arr[i][j] for j in range(m)]
    start_right = [arr[i-1][j] + arr[i][j] for j in range(m)]
        
    # ->
    for j in range(1, m):
        start_left[j] = max(start_left[j], start_left[j-1] + arr[i][j])
            
    # <-
    for j in range(m-2, -1, -1):
        start_right[j] = max(start_right[j], start_right[j + 1] + arr[i][j])
        
    for j in range(m):
        arr[i][j] = max(start_left[j], start_right[j])
        

print(arr[-1][-1])