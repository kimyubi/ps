import sys

input = sys.stdin.readline

# 회의의 수 n
n = int(input())

# 각 회의의 시작 시간과 끝나는 시간
informs = []

for _ in range(n):
    s, e = map(int, input().split())
    informs.append([s,e])

informs = sorted(informs, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
informs = sorted(informs, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

end = 0
cnt = 0

for x in informs:
    if end <= x[0]:
        cnt += 1
        end = x[1]
        
print(cnt)
    
