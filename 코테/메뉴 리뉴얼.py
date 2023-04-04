from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    tmp = set()
    result = []
    for order in orders:
        tmp.update(list(order))
    answer = defaultdict(list)
    
    for c in course:
        for com in combinations(tmp, c):
            cnt = 0
            for order in orders:
                is_contain = True
                for x in com:
                    if x not in order:
                        is_contain = False
                        break
                
                if is_contain:
                    cnt += 1
                    
            if cnt >= 2:
                answer[c].append([com, cnt])
        
        
    result = []
    for x in answer:
        for i in answer[x]:
            if i[-1] == max([t[-1] for t in answer[x]]):
                result.append(''.join(sorted(i[0])))
                
    return sorted(result)

            
                    
        