# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist
from itertools import permutations
def solution(n, weak, dist):
    weak_len, dist_len = len(weak), len(dist)
    answer = dist_len + 1
    
    # 원형 리스트를 선형 리스트로 변환한다.
    weak += [x + n for x in weak]

    for start in range(weak_len):
        for friend in permutations(dist, dist_len):
            count = 1
            reachable_position = weak[start] + friend[count -1]
            
            for i in range(start, start + weak_len):
                if reachable_position < weak[i]:
                    count += 1
                    if dist_len < count:
                        break
                    reachable_position = weak[i] + friend[count - 1]
        
            answer = min(answer, count)
            
    if answer == dist_len + 1:
        return -1
    return answer