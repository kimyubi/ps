# 시간 초과
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    result = [0,0] # 0이 호출되는 횟수, 1이 호출되는 횟수, 피보나치 수 
    def dfs(n):
        global result
        
        if n == 0:
            result[0] += 1
            return 0
        
        if n == 1:
            result[1] += 1
            return 1

        return dfs(n-2) + dfs(n-1)
        
    dfs(n)
    print(result[0], result[1])