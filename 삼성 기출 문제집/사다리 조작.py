import sys
from itertools import combinations
from collections import defaultdict
from copy import deepcopy

input = sys.stdin.readline

# 세로 선의 개수 n, 가로 선의 개수 m, 세로선마다 가로선을 놓을 수 있는 위치의 개수 3
n, m, h = map(int, input().split())
data = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    # b번 세로선과 b+1 세로선을 a번 점선 위치에서 연결
    data[b].append(a)
    
dedicates = []
for i in range(1, n):
    for j in range(1, h + 1):
        if i == 1:
            if j not in data[i + 1] and j not in data[i]:
                dedicates.append([i, j])
                
        elif i == n-1:
            if j not in data[i-1] and j not in data[i]:
                dedicates.append([i, j])
                
        else:
            if  j not in data[i-1] and j not in data[i+1] and j not in data[i]:
                dedicates.append([i, j])
       
def check(copy_data):
    result = True
    
    for idx in range(1, n + 1):
        c = idx
        r  = 1
        while True:
            if h < r:
                break
            if c == 1:
                if r in copy_data[c]:
                    c += 1    
            elif c == n:
                if r in copy_data[c-1]:
                    c -= 1
            else:
                if r in copy_data[c-1]:
                    c -= 1
               
                elif r in copy_data[c]:
                    c += 1
            r += 1
                    
        if idx != c:
            return False
        
    return result            
        

def solution():        
    answer = 4
    for cnt in range(4):
        for comb in combinations(dedicates, cnt):
            copy_data = deepcopy(data)
            for b, a in comb:
                copy_data[b].append(a)
                
            if check(copy_data):
                return cnt
    return -1
            
    
print(solution())