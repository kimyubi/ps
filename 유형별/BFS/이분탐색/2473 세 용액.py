import sys

# 전체 용액의 수 n
n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

def solution(solutions):
    result = []
    
    for i in range(n-2):
        start, end = i+1, n-1
        
        while start < end:
            sum = solutions[i] + solutions[start] + solutions[end]
            
            if sum == 0:
                print(solutions[i],  solutions[start], solutions[end])
                sys.exit(0)
            
            if not result or result[-1][0] > abs(sum):
                result.append([abs(sum), solutions[i],  solutions[start], solutions[end]])
                
            if sum > 0:
                end -= 1
                
            elif sum < 0:
                start += 1
                
    return result[-1][1::]
            
result = solution(solutions)
print(*result)
