import sys

input = sys.stdin.readline

# 전체 용액의 수 n
n = int(input())

# 용액의 특성 값을 나타내는 n개의 정수가 오름차순으로 입력된다.
solution = list(map(int, input().split()))

value = []

start = 0
end = n-1

while start < end:   
    new_value = abs(solution[start] + solution[end])
    
    if len(value) == 0:
        value.append([new_value, start, end])
        
    else:
        if value[-1][0] > new_value:
            value.pop()
            value.append([new_value, start, end])
            
    # 용액의 합이 음수이고
    if solution[start] + solution[end] < 0:
        start += 1
            
    else:
        end -= 1
   
  
    
x, y = value[0][1], value[0][2]
        
print(solution[x], solution[y])
            

