import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# 학생의 수
n = int(input())
skills = list(map(int, input().split()))

sum_skills = []
for i in range(n-1):
    for j in range(i+1, n):
        sum_skills.append([skills[i] + skills[j], i, j])
        
results = []
for sum in sum_skills:
    for idx, skill in enumerate(skills):
        if sum[0] + skill == 0:
            if idx not in sum[1::]:
                results.append([idx, sum[1],sum[2]])
                

results = list(set([tuple(set(result)) for result in results]))
print(len(results))