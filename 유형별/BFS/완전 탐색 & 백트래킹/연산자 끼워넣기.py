import sys
input = sys.stdin.readline

# 수의 개수 n
n = int(input())
arr = list(map(int, input().split()))

# 나눗셈은 정수 나눗셈으로 몫만 취한다.  
# 음수를 양수로 나눌 때는 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
plus, minus, multiple, divide = map(int, input().split())
MAX, MIN = -1*10**9, 10 ** 9

def dfs(plus, minus, multiple, divide, cnt, result):
    global MAX, MIN
    if cnt == n-1:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
        
    if plus:
        dfs(plus-1, minus, multiple, divide, cnt + 1, result + arr[cnt +1])
    if minus:
        dfs(plus, minus-1, multiple, divide, cnt + 1, result - arr[cnt +1])
    if multiple:
        dfs(plus, minus, multiple-1, divide, cnt + 1, result * arr[cnt +1])
    if divide:
        tmp = result // arr[cnt + 1]
        if result < 0:
            tmp = abs(result) // arr[cnt + 1]
            tmp *= -1
        dfs(plus, minus, multiple, divide-1, cnt + 1, tmp)

dfs(plus, minus, multiple, divide, 0, arr[0])
print(MAX)
print(MIN)