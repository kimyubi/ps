from itertools import combinations_with_replacement
def solution(n, apeach_info):
    answer = [-1]
    max_differnece = -1
    for comb in combinations_with_replacement(range(11), n):
        lion_info = [0] * 11
        for score in comb:
            lion_info[10-score] += 1
        
        a, l = 0, 0
        for score, (a_arrow, l_arrow) in enumerate(zip(apeach_info, lion_info)):
            if a_arrow == l_arrow == 0:
                continue
            if a_arrow < l_arrow:
                l += (10 - score)
            else:
                a += (10 - score)
        
        if a < l:
            if max_differnece < l - a:
                max_differnece = l - a
                answer = lion_info
                
    return answer