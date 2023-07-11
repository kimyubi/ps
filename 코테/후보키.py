from itertools import combinations
def is_d_contains_com(d, com):
    result = True
    for c in com:
        if c not in d:
            return False
    return result

def solution(relation):
    answer = 0
    columns = []
    dedicate_index = [i for i in range(len(relation[0]))]
    # 1개의 column으로 구성된 후보 키의 개수
    for idx, x in enumerate(zip(*relation[::-1])):
        if len(set(x)) == len(x):
            answer += 1
            dedicate_index.remove(idx)
        columns.append(list(x))

    dedicate = dedicate_index[:]
    morethan2Dediacate = []
    # 2 ~ 8 개의 column으로 구성된 후보 키의 개수
    for i in range(2, len(columns)):
        for com in combinations(dedicate, i):
            morethan2Dediacate.append(list(com))
            
    for com in morethan2Dediacate:
        tuple = [columns[i] for i in com]
        tmp = []
        for x in zip(*tuple):
            tmp.append(''.join(x))
        # 후보키 등록
        if len(set(tmp)) == len(tmp):
            answer += 1
            for d in morethan2Dediacate:
                if is_d_contains_com(d, com):
                    morethan2Dediacate.remove(d)
    return answer