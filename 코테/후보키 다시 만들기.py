from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    #유일성
    unique = []
    for com in combi:
        tmp = [tuple([item[key] for key in com]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            is_dedicate = True
            
            for x in unique:
                if set(x).issubset(set(com)):  # 최소성
                    is_dedicate = False
                    break
                    
            if is_dedicate: unique.append(com)
   
    return len(unique)