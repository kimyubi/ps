# 12:15 ~
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

info = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    info.append([r-1, c-1, m, s, d])

for _ in range(k):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    
    for r, c, m, s, d in info:
        nr, nc = (r + dx[d] * s) % n , (c + dy[d] * s) % n
        graph[nr][nc].append([m, s, d])
           
    info.clear()
    for i in range(n):
        for j in range(n):
            cnt = len(graph[i][j])
            if 2 <= cnt:
                is_odd, is_even = 0, 0 
                nm, ns = 0, 0
                for m, s, d in graph[i][j]:
                    nm += m
                    ns += s
                    
                    if d % 2 == 0:
                        is_even +=1
                    else:
                        is_odd += 1
                                            
                nm //= 5
                ns //= cnt
                
                if is_odd == cnt or is_even == cnt:
                    nd = [0, 2, 4, 6]        
                else:
                    nd = [1, 3, 5, 7]
                
                if nm:
                    for k in nd:
                        info.append([i, j, nm, ns, k])
        
            elif cnt == 1:
                m, s, d = graph[i][j][0]
                info.append([i, j, m, s, d])
answer = 0
for r, c, m, s, d in info:
    answer += m
print(answer)            
             
                 
    