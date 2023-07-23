from collections import deque

info = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

# 탈출까지 이동해야 하는 거리 k
def solution(n, m, x, y, r, c, k):
    x, y, r, c = x-1, y-1, r-1, c-1
    answer = ''
    
    queue = deque()
    queue.append([x, y, '', 0])

    while queue:
        x, y, path, dist = queue.popleft()
        
        if (x,y) == (r,c):
            if dist == k:
                return path
            elif (k - dist) % 2 == 1:
                return 'impossible'
        
        for i in range(4):
            nx, ny, ndist = x + dx[i], y + dy[i], dist + 1
            
            if 0 <= nx < n and 0 <= ny < m:
                if abs(nx - r) + abs(ny - c) + ndist <= k:
                    queue.append([nx, ny, path + info[i], ndist])
                    break
                
    return "impossible"