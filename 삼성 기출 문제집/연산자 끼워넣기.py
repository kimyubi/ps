import sys

input = sys.stdin.readline

# 수의 개수 n
n = int(input())
numbers = [0] + list(map(int, input().split()))

max_result = -sys.maxsize
min_result = sys.maxsize

# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
plus, minus, multiple, division = map(int, input().split()) 

def dfs(depth, result, plus, minus, multiple, division):
    global max_result, min_result
    
    if n == depth:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if plus:
        dfs(depth + 1, result + numbers[depth + 1], plus-1, minus, multiple, division)
    
    if minus:
        dfs(depth + 1, result - numbers[depth + 1], plus, minus -1, multiple, division)
        
    if multiple:
        dfs(depth + 1, result * numbers[depth + 1], plus, minus, multiple -1, division)
        
    if division:
        if result < 0:
            result = (abs(result) // numbers[depth + 1]) * -1
        else:
            result //= numbers[depth + 1]
        dfs(depth + 1, result, plus, minus, multiple, division-1)




dfs(1, numbers[1], plus, minus, multiple, division)
print(max_result, min_result, end='\n')