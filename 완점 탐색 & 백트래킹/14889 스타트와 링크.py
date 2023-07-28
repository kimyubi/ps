import sys
from itertools import combinations
input = sys.stdin.readline

# 인원 n (짝수)
n = int(input())
skill = [list(map(int, input().split())) for _ in range(n)]
people = {i for i in range(n)}
answer = 10 ** 6

for team1 in combinations(people, n//2):
    team2 = people - set(team1)
    
    # 첫번째 팀의 능력치 합 구하기
    team1_skill = 0
    for x, y in combinations(team1, 2):
        team1_skill += skill[x][y] + skill[y][x]
    
    # 두번째 팀의 능력치 합 구하기
    team2_skill = 0
    for x, y in combinations(team2, 2):
        team2_skill += skill[x][y] + skill[y][x]
        
    answer = min(answer, abs(team1_skill - team2_skill))
print(answer)
    