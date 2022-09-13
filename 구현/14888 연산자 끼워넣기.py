from sys import maxsize

n = int(input())
numbers = list(map(int, input().split()))

# 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수
operator = list(map(int, input().split()))

min_value = maxsize
max_value = -maxsize

def dfs(depth, sum, plus, minus, multiple, divide):
    global min_value, max_value
    
    if depth == n:
        min_value = min(min_value, sum)
        max_value = max(max_value, sum)
        return
        
    
    if plus:
        dfs(depth + 1, sum + numbers[depth], plus - 1, minus, multiple, divide)
    
    if minus:
        dfs(depth + 1, sum - numbers[depth], plus, minus - 1, multiple, divide)
        
    if multiple:
        dfs(depth + 1, sum * numbers[depth], plus, minus, multiple - 1, divide)
        
    if divide:
        dfs(depth + 1, int(sum / numbers[depth]), plus, minus, multiple, divide - 1)
    
         

dfs(1, numbers[0], operator[0], operator[1], operator[2], operator[3])

print(max_value)
print(min_value)