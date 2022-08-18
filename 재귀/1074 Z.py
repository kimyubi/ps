# n : 한 변의 길이
def solution(n, x, y):
    global answer
    
    if x == r and y == c:
        print(int(answer))
        exit(0)
        
    if n == 1:
        answer += 1
        return
    
    if not (x <= r < x + n and y <= c < y + n):
        answer += n ** 2    
        return
    
    half = n/2
    
    solution(half,x,y)
    solution(half,x,y+half)
    solution(half,x+half,y)
    solution(half,x+half,y+half)
    
    


n, r, c = map(int, input().split())
answer = 0
solution(2 ** n, 0, 0)