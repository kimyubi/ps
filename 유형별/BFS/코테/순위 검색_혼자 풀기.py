from collections import defaultdict
from itertools import combinations
import bisect

def get_all_case(informations, info_dic):
    for info in informations:
        arr = info.split()
        case = arr[:-1]
        score = int(arr[-1])
        
        for i in range(5):
            for c in combinations(case, i):
                key = ''.join(c)
                info_dic[key].append(score)
                
    for key in info_dic.keys():
        info_dic[key].sort()
    
    return info_dic

def find_answer(key, score, info_dic):
    if key in info_dic:
        return len(info_dic[key]) - bisect.bisect_left(info_dic[key], score)
    return 0
    
def solution(informations, queries):
    answer = []
    
    # 각 info가 통과할 수 있는 모든 케이스를 구해 딕셔너리에 키(케이스), 값(점수) 형태로 저장한다.
    info_dic = get_all_case(informations, defaultdict(list))

    for query in queries:
        query = query.replace("and", "").replace("-", "").split()
        score = int(query[-1])
        
        if len(query) == 1:
            answer.append(find_answer('', score, info_dic))
        else:
            answer.append(find_answer(''.join(query[:-1]), score, info_dic))
        
    return answer