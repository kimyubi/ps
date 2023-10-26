import sys

input = sys.stdin.readline

L, P, V = map(int, input().split())
i = 1 
while L != 0 and P != 0 and V != 0:
    x =  V % P
    if x > L: x = L
    print("Case %d: %d" % (i, ((V//P) * L) + x))
    i += 1
    L, P, V = map(int, input().split())