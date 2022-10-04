import sys
input = sys.stdin.readline

n = int(input())
l = []

for i in range(n):
    x = str(input().rstrip())
    
    sum = 0
    for k in x:
        if str.isdigit(k):
            sum += int(k)
    
    l.append([len(x), sum, x])


l.sort(key = lambda x: (x[0], x[1], x[2]))

for x in l:
    print(x[2])    