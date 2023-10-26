import sys

input = sys.stdin.readline
println = sys.stdout.write

n = int(input())

values = [0] * 10001

for i in range(n):
    x = int(input())
    values[x] += 1

for i in range(1, 10001):
    if values[i] != 0:
        
        for j in range(values[i]):
            println(str(i) + '\n')
            
    
    
    

