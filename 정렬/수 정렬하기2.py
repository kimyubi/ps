import sys

input = sys.stdin.readline
println = sys.stdout.write

n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))  

for x in sorted(values):
    println(str(x) + '\n')
    
    

