import sys

input = sys.stdin.readline

# 테스트 케이스의 수 t
t = int(input())


def dfs(x,depth):
    global ans
    
    if x == n:
        ans += 1 
        return
    
    if depth == n:
        return
    
    for i in range(1, 4):
        dfs(x+i, depth+1)
    

result = []
for _ in range(t):
    n = int(input())
    ans = 0
    dfs(0,0)
    
    result.append(ans)


print(*result, sep='\n')