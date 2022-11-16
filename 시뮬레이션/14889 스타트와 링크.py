from itertools import combinations, permutations
import sys

input = sys.stdin.readline

ans = sys.maxsize

# 축구를 하기 위해 모인 사람의 수 n (짝수)
n = int(input())

# 능력치 그래프
s = [list(map(int, input().split())) for _ in range(n)]

player = set([i for i in range(0, n)])


# n/2명의 조합을 선택해 하나의 팀을 만들고, 선택되지 않은 n/2명으로 두번째 팀을 만든다. 
# 순서를 고려하지 않으므로, 조합 이용
for com in combinations(player, n//2):
    com = set(com)
    start = list(com)
    link = list(player-com)
    
    
    # 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
    # i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
    # => 순서를 고려해야하므로, 순열 이용
    start_stats = 0
    for x in permutations(start, 2):
        start_stats += s[x[0]][x[1]]
        
    link_stats = 0
    for y in permutations(link, 2):
        link_stats += s[y[0]][y[1]]
        
    ans = min(ans, abs(start_stats - link_stats))

print(ans)    
    