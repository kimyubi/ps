import sys
input = sys.stdin.readline

# 지도의 크기 n, 경사로의 길이 l
n, l  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]    
visited = [[False] * n for _ in range(n)]


def rotate(graph):
    result = []
    for x in zip(*graph[::-1]):
        result.append(list(x))
    return result

answer = 0
def solution(graph):
    global answer, visited
    
    for idx, row in enumerate(graph):
        # 길에 속한 모든 칸의 높이가 모두 같다면 지나갈 수 있다.
        if len(set(row)) == 1:
            answer += 1
            continue
        
        
        now = 0
        next = now + 1
        passible_path = True
        
        while True:
            if not (0 <= next < n):
                break 
            
            # 현재 칸과 다음 칸의 높이가 같은 경우 전진한다.
            if row[now] == row[next]:
                now = next
                next = now + 1
                continue
            
            # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
            if 1 < abs(row[now] - row[next]):
                passible_path = False
                break
            
            # 현재 칸이 1 높은 경우, 다음 칸에 길이가 l인 경사로를 놓는다.
            if row[next] < row[now]:
                # 경사로를 놓고자 하는 자리에 이미 설치된 경사로가 있는지 확인한다.
                # 1. 경사로를 놓다가 범위를 벗어나는 경우, 경사로를 놓을 수 없으므로 그 길을 지나갈 수 없다.
                # 2. 이미 설치된 경사로가 있다면 새로 경사로를 놓을 수 없으므로, 그 길을 지나갈 수 없다.
                # 3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                lower_height = row[next]
                for i in range(l):
                    # 1. 
                    if not (0 <= next + i < n):
                        passible_path = False
                        break
                    
                    # 2. 
                    if visited[idx][next + i]:
                        passible_path = False
                        break
                    
                    # 3.
                    if row[next + i] != lower_height:
                        passible_path = False
                        break
                    
                    # 경사로 설치
                    visited[idx][next + i] = True
                    
                if not passible_path:
                    break
                
                now += l
                next = now + 1
                
            # 다음 칸이 1 높은 경우, 현재 칸에 길이가 l인 경사로를 놓는다.
            else:
                lower_height = row[now]
                for i in range(l):
                    # 1. 
                    if not (0 <= now - i < n):
                        passible_path = False
                        break
                    
                    # 2. 
                    if visited[idx][now - i]:
                        passible_path = False
                        break
                    
                    # 3.
                    if row[now - i] != lower_height:
                        passible_path = False
                        break
                    
                    # 경사로 설치
                    visited[idx][now - i] = True
                    
                if not passible_path:
                    break
                
                now = next
                next = now + 1
                   
        if passible_path:
            answer += 1
        
        
solution(graph)
visited = [[False] * n for _ in range(n)]
solution(rotate(graph))
print(answer)

