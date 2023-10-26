import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
a,b = 0, 0

def solution(n):
    global a, b
    
    # n이 1인 경우
    if n == 1:
        print('A')
        return
    
    # n이 2인 경우
    if n == 2:
        if arr[0] == arr[1]:
            print(arr[0])
            return
        
        else:
            print('A')
            return
        
    
    # n이 3 이상인 경우
    if n >= 3:
        # Zero division Error 방지
        if (arr[1] - arr[0]) == 0:
            a = 0
        
        else: 
            a = (arr[2] - arr[1]) // (arr[1] - arr[0])
        
        b = arr[1] - arr[0] * a        
        
        for i in range(n - 1):
            if arr[i + 1] == arr[i] * a + b:
                continue
            
            else:
                print('B')
                return
    
    return True

if solution(n):
    print(arr[-1] * a + b)

    