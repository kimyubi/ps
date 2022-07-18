import sys
input = sys.stdin.readline

while True:
    stack = list()
    result = 0
    
    heights = list(map(int, input().split()))
    if heights[0] == 0:
        break
    
    height_list = heights[1::] + [0]
    
    for i, height in enumerate(height_list):
        idx = i
        while stack and stack[-1][0] > height:
            h, idx = stack.pop()
            result = max(result, (i-idx) * h)
        
        # 왜 stack.append((height,i)) 가 아니라 stack.append((height, idx)) 인지 모르겠음
        stack.append((height, idx))
    
    print(result)

