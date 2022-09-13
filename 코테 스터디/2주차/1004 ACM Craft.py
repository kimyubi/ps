import sys
from collections import deque

input = sys.stdin.readline

# 테스트케이스의 갯수
T = int(input())

for _ in range(T):
    # 건물의 개수 n과 건물간의 건설순서 규칙의 총 개수 k
    n, k = map(int, input().split())
    
    time = [0] + list(map(int, input().split())) # 건물들의 건설 시간
    seq = [[] for _ in range(n + 1)] # 건설순서 규칙
    inDegree = [0 for _ in range (n + 1)] # 진입차수
    DP = [0 for _ in range (n+1)] # 해당 건물까지 걸리는 시간 저장
    
    
    for _ in range(k):
        a, b = map(int, input().split())
        seq[a].append(b)
        
        inDegree[b] += 1 
        
    
    queue = deque()
    #진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            DP[i] = time[i]
            
    
    while queue:
        now = queue.popleft()
        
        for i in seq[now]:
            inDegree[i] -= 1
            
            DP[i] = max(DP[now] + time[i], DP[i])
            
            if inDegree[i] == 0:
                queue.append(i)
    
    
    # 백준이가 승리하기 위해 건설해야 할 건물의 번호 W
    w = int(input())
    print(DP[w])