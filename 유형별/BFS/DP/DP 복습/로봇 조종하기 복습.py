import sys
input = sys.stdin.readline

# n개의 줄에 m개의 수로 배열이 주어진다.
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    arr[0][i] += arr[0][i-1]
    

for i in range(1, n):
    left_start = [arr[i-1][j] + arr[i][j] for j in range(m)]
    right_start = [arr[i-1][j] + arr[i][j] for j in range(m)]
    
    # -> 
    for j in range(1, m):
        left_start[j] = max(left_start[j], left_start[j-1] + arr[i][j])

    # <-
    for j in range(m-2, -1, -1):
        right_start[j] = max(right_start[j], right_start[j+1] + arr[i][j])
        
    for j in range(m):
        arr[i][j] = max(left_start[j], right_start[j])
        

print(arr[-1][-1])