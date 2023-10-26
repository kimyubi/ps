import heapq
def solution(operations):
    # 힙은 맨 마지막 리프 노드가 최댓값임을 보장하지 않는다.
    heap = []
    heapq.heapify(heap)
    
    for operation in operations:
        command, data = operation.split()
        data = int(data)
        
        if command == "I":
            # 큐에 주어진 숫자를 삽입한다.
            heapq.heappush(heap, data)
        else:
            if heap:
                # 큐에서 최댓값을 삭제한다.
                if data == 1:
                    heap.remove(max(heap))
                    
                # 큐에서 최솟값을 삭제한다.
                else:
                    heapq.heappop(heap)
                    
    
    if not heap:
        return [0,0]
    else:
        return [max(heap), heap[0]]
    
