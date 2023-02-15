import sys

input = sys.stdin.readline

# 마을 수 n, 트럭의 용량 c
n, c = map(int, input().split())

# 보내는 박스 정보의 개수 m
m = int(input())

# 보내는 마을, 받는 마을, 박스의 개수
info = [list(map(int, input().split())) for _ in range(m)]
info.sort(key= lambda x: [x[1], x[0]])

boxes = [0] * (n+1)
ans = 0

for s, r, box in info:
    max_box = box
    
    for i in range(s, r):
        max_box = min(max_box, c - boxes[i])
    
    for i in range(s, r):
        boxes[i] += max_box
        
    ans += max_box
    
print(ans)
        
    
    


