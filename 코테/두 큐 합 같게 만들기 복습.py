from collections import deque
def solution(queue1, queue2):
    answer =  0 
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    # 두 큐의 합이 홀수이면, 두 큐의 합을 같게 만들 수 없다.
    if sum1 + sum2 % 2 == 1:
        return -1
    
    # 4 * n(큐의 길이)번 insert & pop을 수행하면 처음 큐 상태로 돌아간다.
    for i in range(len(queue1) * 4):
        # sum1이 sum2보다 크면, queue1의 원소를 추출하여 queue2에 삽입힌다.
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
            
        # sum2가 sum1보다 크면, queue2의 원소를 추출하여 queue1에 삽입한다.
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        
        # sum1과 sum2가 같은 경우
        else:
            return i
    
    return -1