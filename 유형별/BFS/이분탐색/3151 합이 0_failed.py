import sys
from itertools import combinations
input = sys.stdin.readline


# 학생의 수
n = int(input())
skills = list(map(int, input().split()))
skills.sort()

print(skills)