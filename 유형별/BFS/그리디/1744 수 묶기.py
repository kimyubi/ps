import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

answer = 0

numbers = deque(numbers)
negative = []

# 음수, 0 / 양수를 분리
while numbers:
    if numbers[0] <= 0:
        negative.append(numbers.popleft())
    else:
        break


# 음수/ 0 처리
if len(negative) % 2 != 0:
    answer += negative.pop()
    
for i in range(0, len(negative)-1 , 2):
    answer += negative[i] * negative[i+1]
    
        
# 양수 처리
if len(numbers) % 2 != 0:
    answer += numbers.popleft()
    
for i in range(0, len(numbers)-1 , 2):
    # 1 3일 경우 서로 곱하는 것보다 더한 값이 더 크다.
    answer += max(numbers[i] + numbers[i+1], numbers[i] * numbers[i+1])



print(answer)