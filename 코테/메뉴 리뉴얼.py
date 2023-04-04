from itertools import combinations
from collections import Counter, defaultdict

def solution(orders, course):  
    answer = []
    for course_size in course:
        order_comb = []
        
        for order in orders:
            if course_size <= len(order):
                order_comb += combinations(sorted(order), course_size)
        
        most_ordered = Counter(order_comb).most_common()
        answer += [''.join(k) for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    
    return sorted(answer)

    
   
            