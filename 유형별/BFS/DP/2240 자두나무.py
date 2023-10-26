import sys
input = sys.stdin.readline

T,W = map(int, input().split())
position = 1
cnt = 0

while True:
    if W <= 0 :
        break
    
    num = int(input())
    if position == num:
        cnt += 1
    else:
        position = 3 - position
        W -= 1
        cnt +=1

print(cnt)