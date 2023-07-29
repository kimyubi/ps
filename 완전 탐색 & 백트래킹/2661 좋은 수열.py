import sys
input = sys.stdin.readline

n = int(input())
numbers = ''
answer = int('3' * 80) + 1

# 12131 12132 12121
def dfs(numbers):
    global answer
    if 2 <= len(numbers):
        if numbers[-1] == numbers[-2]:
            return
        for i in range(2, len(numbers)//2 + 1):
            if numbers[-i:] == numbers[-i * 2:-i]:
                return
                
    
    if len(numbers) == n:
        print(numbers)
        exit(0)
    
    dfs(numbers + '1')
    dfs(numbers + '2')
    dfs(numbers + '3')
    
dfs(numbers)

