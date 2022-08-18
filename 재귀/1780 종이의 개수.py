import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

minus, zero, one = 0, 0, 0

def solution(x,y,length):
    global minus, zero, one
    
    for i in range(x, x + length):
        for j in range(y, y + length):
            if graph[x][y] != graph[i][j]:
                
                for s in range(3):
                    for k in range(3):
                        solution(x + length//3*s , y + length//3 * k ,length//3)
            
                return
        
    if graph[x][y] == -1:
       minus += 1
    
    elif graph[x][y] == 0:
        zero += 1
        
    else:
        one += 1
    
    


solution(0,0,n)
print(minus)
print(zero)
print(one)