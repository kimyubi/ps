import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
zero, one = 0,0

def solution(x,y,length):
    global zero, one
    
    for i in range(x, x + length):
        for j in range(y, y + length):
            if graph[x][y] != graph[i][j]:
                for a in range(2):
                    for b in range(2):
                        solution(x + length//2 * a, y + length //2 * b, length//2)
    
                return
        
    
    if graph[x][y] == 0:
        zero += 1
        
    else:
        one += 1
    


solution(0,0,n)

print(zero)
print(one)
