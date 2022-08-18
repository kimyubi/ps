# n: 원반의 개수, start: 옮기고자 하는 대상의 위치, end: 대상을 옮길 위치
def hanoi_tower(n, start, end) :
    # 원반이 1개면 옮기고자 하는 위치로 그냥 옮긴다.
    if n == 1 :
        print(start, end)
        return  
    
    temp = 6 - start - end
    hanoi_tower(n-1, start, temp) 
    print(start, end) 
    hanoi_tower(n-1, temp, end) 
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
    
    
    
    