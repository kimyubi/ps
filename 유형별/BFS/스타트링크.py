from collections import deque
import sys

input = sys.stdin.readline
F,S,G,U,D = map(int, input().split())

visited = [0] * F * 2
queue = deque()
queue.append(S)
visited[S] = 1

while queue:
    x = queue.popleft()
    
    for i in (+U, -D):
        nx = x + i
            
        if 0 < nx <= F and not visited[nx]:
            visited[nx] = visited[x] + 1
            queue.append(nx)
            
if visited[G] == 0:
    print("use the stairs")
else:
    print(visited[G] -1)

print(visited)