import sys
input = sys.stdin.readline

n = int(input())
level = [int(input()) for _ in range(n)]

max = level.pop()
answer = 0

for i in range(len(level) -1, -1, -1):
    while max <= level[i]:
        level[i] -= 1
        answer += 1
    
    max = level[i]
    
print(answer)