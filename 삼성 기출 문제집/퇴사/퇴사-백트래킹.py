import sys
input = sys.stdin.readline

# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
N = int(input())
T, P = [0], [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
    
answer = 0
def solution(idx, sum):
    global answer
    
    # 종료 조건
    if N < idx:
        answer = max(answer, sum)
        return
    
    # 퇴사일 이내에 가능할때 상담
    if idx + T[idx] <= N + 1:
        solution(idx + T[idx], sum + P[idx])
        
    solution(idx + 1, sum)
        


solution(1, 0)
print(answer)
