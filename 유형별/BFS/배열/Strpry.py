from collections import Counter

n = int(input())

for _ in range(n):
    x,y = input().split()
    cnt_x = Counter(x)
    cnt_y = Counter(y)
    
    if len((cnt_x - cnt_y).keys()) == 0 and len((cnt_y - cnt_x).keys()) == 0:
        print("Possible")
    
    else:
        print("Impossible")