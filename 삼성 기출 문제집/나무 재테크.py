import sys
input = sys.stdin.readline

# n : 땅의 크기, m: 나무의 개수 
n, m, k = map(int, input().split())

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
nourishment = [[5] * n for _ in range(n)]

# 겨울마다 추가되는 양분의 양
plus_nourishment = [list(map(int, input().split())) for _ in range(n)]

# tree_info : 나무의 정보 
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
tree_info = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    # (x, y) : 나무의 위치, age: 나무의 나이
    x, y, age = map(int, input().split())
    tree_info[x-1][y-1].append(age)
    
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    
for _ in range(k):
    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            # 해당 칸에 나무가 있다면
            if tree_info[i][j]:
                # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
                tree_info[i][j].sort()
                
                live_tree_info = []
                dead_tree_to_nourishment = 0
                for age in tree_info[i][j]:
                    # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다
                    if age <= nourishment[i][j]:
                        nourishment[i][j] -= age
                        live_tree_info.append(age + 1)
                        continue
                        
                    # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                    # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다
                    else:
                        dead_tree_to_nourishment += age //2
                  
                tree_info[i][j] = live_tree_info
                nourishment[i][j] += dead_tree_to_nourishment
                
    # 가을 + 겨울
    for i in range(n):
        for j in range(n):
            if tree_info[i][j]:
                for age in tree_info[i][j]:
                    # 가을에는 나무가 번식한다.
                    # 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                    if age % 5 == 0:
                        for d in range(8):
                            ni, nj = i + dx[d], j + dy[d]
                            
                            # 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                            if 0 <= ni < n and 0 <= nj < n:
                                tree_info[ni][nj].append(1)
                   
            # S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.              
            nourishment[i][j] += plus_nourishment[i][j]                     
            
answer = 0  
for i in range(n):
    for j in range(n):
        answer += len(tree_info[i][j])
        
print(answer)
                                      
                            
                    
                
                    
                
    