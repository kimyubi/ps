# 흰 점을 나타내는 0, 검은 점을 나타내는 1
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]

def solution(x,y,length):
    global answer
    
    for i in range(x, x + length):
        for j in range(y, y + length):
            if graph[x][y] != graph[i][j]:
                answer += '('
                for a in range(2):
                    for b in range(2):
                        solution(x + length//2*a, y + length//2*b, length//2)
                
                answer += ')'        
                return
    
    answer += str(graph[x][y]) 
   
    
    


answer = ''
solution(0,0,n)

print(answer)