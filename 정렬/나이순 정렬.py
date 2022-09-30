import sys

input = sys.stdin.readline
n = int(input())
l = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    
    l.append([age,name,i])
    

l.sort(key = lambda x: (x[0], x[2]))

for x in l:
    print(x[0], x[1])

    
    