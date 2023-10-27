import sys
from copy import deepcopy
input = sys.stdin.readline

# 보드의 크기 n
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 한번의 이동 : 보드 위에 있는 전체 블록을 상하좌우 네방향중 하나로 이동
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐진다.
# 한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 합쳐질 수 없다.
# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def move(board, direction):
    return

answer = 0  
def solution(board, depth):
    global answer
    if depth == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return
        
    for i in range(4):
        solution(move(deepcopy(board), i), depth + 1)
        
solution(board, 0)    
print(answer)
        
    
                
            
            
            