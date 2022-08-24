import sys
input = sys.stdin.readline
n = int(input())

# 깨진 계란의 개수
def check(eggs):
    count = 0
    
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
            
    return count

def dfs(index, eggs):
    global answer
    
    if index == n:
        answer = max(answer, check(eggs))
        return
    
    # 현재 왼 쪽에 든 계란이 깨져있다면, 내려놓고 한 칸 오른쪽 계란을 왼쪽에 든다.
    if eggs[index][0] <= 0:
        dfs(index + 1, eggs)
        
    else:
        is_all_broken = True
        
        # 상대 계란 선택
        for i in range(n):
            # 현재 왼쪽에 든 계란, 이미 깨져있는 계란 제외
            if index != i and eggs[i][0] > 0:
                
                # 상대 계란이 하나라도 선택되면 모든 계란이 깨져있는 경우가 아니므로
                is_all_broken = False
                
                eggs[index][0] -= eggs[i][1]
                eggs[i][0] -= eggs[index][1]
                
                dfs(index+1, eggs)
                
                # dfs를 빠져나오면 계란을 원상 복구 시켜준다.
                eggs[index][0] += eggs[i][1]
                eggs[i][0] += eggs[index][1]
                
                
        # 모든 계란이 깨져있는 경우 dfs를 빠져나온다.
        if is_all_broken:
            dfs(n, eggs)
        
    
        
    
    


eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dfs(0, eggs)
print(answer)