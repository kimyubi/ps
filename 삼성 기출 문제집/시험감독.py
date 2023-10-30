import sys
input = sys.stdin.readline

# 시험장의 개수 n
n = int(input())

test_centers =  list(map(int, input().split()))
main, sub = map(int, input().split())

result = 0
for candidate_cnt in test_centers:
    if candidate_cnt <= main:
        result += 1 
        continue
    
    else:
        candidate_cnt -= main
        result += 1
        
        if candidate_cnt % sub == 0:
            result += candidate_cnt // sub
            
        else:
            result += candidate_cnt // sub + 1
            
print(result)
    