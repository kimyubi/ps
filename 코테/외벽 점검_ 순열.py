from itertools import permutations
def solution(n, weak, dist):
    weak_len, dist_len = len(weak), len(dist)
    
    # 원형 리스트를 선형 리스트로 변환
    weak += [x + n for x in weak]
    answer = dist_len + 1
    
    for start in range(weak_len):
        for friend_dist in permutations(dist, dist_len):
            # 투입할 친구 수
            count = 1
            # 친구가 이동할 수 있는 최대 지점
            position = weak[start] + friend_dist[count-1]
            
            for i in range(start, start + weak_len):
                if position < weak[i]:
                    count += 1
                    if dist_len < count:
                        break
                    position = weak[i] + friend_dist[count -1]
                    
            answer = min(count, answer)
    
    if answer == dist_len + 1:
        return -1
    return answer