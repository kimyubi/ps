import sys
from bisect import bisect_left, bisect_right

# 학생의 수 n
n = int(input())
students = list(map(int, input().split()))
students.sort()

def count(x):
    left_index = bisect_left(students, x)
    right_index = bisect_right(students, x)
    
    return right_index - left_index

def solution():
    ans = 0
    for i in range(n-1):
        start, end = i+1, n-1
        
        while start < end:
            sum = students[i] + students[start] + students[end]
            
            if sum == 0:
                if students[start] == students[end]:
                    ans += end - start
                else:
                    ans += count(students[end])
                    
                start += 1
            
            elif sum > 0:
                end -= 1
                
            else:
                start += 1
                
    return ans
                
print(solution())
        