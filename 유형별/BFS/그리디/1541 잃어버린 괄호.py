import sys

input = sys.stdin.readline
formula = input().rstrip()

formulas = formula.split('-')

answer = sum(list(map(int, formulas[0].split('+'))))

for i in range(1, len(formulas)):
    answer -= sum(list(map(int, formulas[i].split('+'))))

print(answer)


