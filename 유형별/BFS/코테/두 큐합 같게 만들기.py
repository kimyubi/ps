
# 내 풀이 - 정확성 실패

from collections import deque
def solution(queue1, queue2):
    target = sum(queue1) + sum(queue2)
    
    # 두 큐의 원소 합이 홀수라면
    if target % 2 == 1:
        return -1

    target //= 2
    # 두 큐의 합이 이미 같다면
    if sum(queue1) == sum(queue2) == target:
        return 0
    
    if sum(queue1) < sum(queue2):
        small_queue = deque(queue1)
        large_queue = deque(queue2)
    else:
        small_queue = deque(queue2)
        large_queue = deque(queue1)
    
    answer = 0
    while sum(large_queue) > target:
        x = large_queue.popleft()
        small_queue.append(x)
        answer += 1
    print(small_queue, large_queue)
    while sum(small_queue) > target:
        x = small_queue.popleft()
        large_queue.append(x)
        answer += 1
    print(small_queue, large_queue)
    
    
    if sum(small_queue) == sum(large_queue) == target:
        return answer
    else:
        return -1
        