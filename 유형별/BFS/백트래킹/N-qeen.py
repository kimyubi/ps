# 9663
# 퀸은 같은 행, 같은 열, 대각선 상에 있는 다른 퀸을 공격 가능

import sys
input = sys.stdin.readline

# n*n 체스판에서 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다
# n이 최댓값은 15로 매우 작으므로, 백트래킹 고려
n = int(input())

def is_adjacent(idx):
    for i in range(idx):
        if visited[i] == visited[idx] or abs(visited[idx] - visited[i]) == idx - i:
            return False
        
    return True

def dfs(idx):
    global ans
    
    if idx == n:
        ans += 1
        return
    
    for i in range(n):
        visited[idx] = i
        
        if is_adjacent(idx):
            dfs(idx+1)
        

visited = [0] * n        
ans = 0
dfs(0)

print(ans)

