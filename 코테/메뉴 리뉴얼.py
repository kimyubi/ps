from itertools import combinations
from collections import Counter, defaultdict

def solution(orders, course):
    tmp = []
    
    # 가능한 모든 조합을 찾는다.
    for c in course:
        for order in orders:
            if c <= len(order):
                for x in combinations(order, c):
                    tmp.append(''.join(sorted(x)))
    
    # 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 넣는다.
    counter = Counter(tmp)
    dic = defaultdict(list)
    for x in counter:
        if counter[x] >= 2:
            dic[len(x)].append([x, counter[x]])

    # 요리 n개로 구성된 코스 요리 중 가장 많은 손님에게 주문된 구성만 고른다.
    result = []
    for x in dic:
        for item in dic[x]:
            if item[-1] == max([i[-1] for i in dic[x]]):
                result.append(item[0])
    
    result.sort()
    return result

            