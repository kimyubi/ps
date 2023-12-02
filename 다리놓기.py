import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    r, n = map(int, input().split())
    print(math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))