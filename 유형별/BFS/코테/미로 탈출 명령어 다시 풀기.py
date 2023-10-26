# d l r u
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
info = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}

from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    x, y, r, c = x-1, y-1, r-1, c-1
    
    queue = deque()
    queue.append([x, y, '', 0])
    
    while queue:
        x, y, path, dist = queue.popleft()
        
        if (x, y) == (r, c):
            if dist == k:
                return path
            if (k - dist) % 2 == 1:
                return 'impossible'
        
        for i in range(4):
            nx, ny, ndist = x + dx[i], y + dy[i], dist + 1
            if 0 <= nx < n and 0 <= ny < m:
                # 출발 지점부터 (nx, ny)까지의 거리 + (nx, ny)부터 도착 지점까지의 거리
                # = 탈출까지 이동해야 하는 거리
                if ndist + abs(nx - r) + abs(ny -c) <= k:
                    queue.append([nx, ny, path + info[i], ndist])
                    break
                    
    return 'impossible'