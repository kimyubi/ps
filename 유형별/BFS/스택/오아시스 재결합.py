heights = [int(input()) for _ in range(int(input()))]

stack = [] # (키, cnt)로 append
result = 0

for height in heights:

  # 스택 끝 값보다 키 크면 pop
  while stack and stack[-1][0]<height:
    result += stack.pop()[1]

  # 스택이 비어있으면 해당 키 append하고 continue
  if not stack:
    stack.append((height, 1))
    continue

    
  # 스택 끝 값의 키와 같을 때
  if stack[-1][0]==height:
    cnt = stack.pop()[1]
    result += cnt

    if stack: result += 1
    stack.append((height, cnt+1))

  # 스택 끝 값의 키보다 작을 때
  else:
    stack.append((height, 1))
    result += 1

# 결과값 출력
print(result)