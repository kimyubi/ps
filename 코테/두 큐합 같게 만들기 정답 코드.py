from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    # 두 큐의 합이 홀수이면, 두 큐의 합이 같을 수 없다.
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    # (큐의 길이 * 4)번 이동하면 queue1과 queue2가 원래 상태로 돌아가기 때문에 같은
    # 작업을 반복하게 된다. 
    for _ in range(len(queue1) * 3):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
            
        elif sum1 < sum2:
            sum2 -= queue2[0]
            sum1 += queue2[0]
            queue1.append(queue2.popleft())
            
            
        else:
            return answer
        
        answer += 1
        
    return -1
    
    
