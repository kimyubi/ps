# J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
from collections import Counter
def solution(str1, str2):
    answer = 0
    tmp1, tmp2 = [], []
    
    for i in range(len(str1) - 2 + 1):
        if str1[i:i+2].isalpha():
            tmp1.append(str1[i:i+2].lower())
    
    for i in range(len(str2) - 2 + 1):
        if str2[i:i+2].isalpha():
            tmp2.append(str2[i:i+2].lower())
    
    str1, str2 = tmp1, tmp2
    
    if len(str1) == len(str2) == 0:
        return 65536
    
    dic1 = dict(Counter(str1))
    dic2 = dict(Counter(str2))
    
    union, intersection = [], []
    
    for key1 in dic1.keys():
        for key2 in dic2.keys():
            if key1 == key2:
                # 교집합 구하기
                intersection.extend([key1] * min(dic1[key1], dic2[key2]))
                
                # 합집합 구하기
                union.extend([key1] * max(dic1[key1], dic2[key2]))
            
            else:
                if key1 not in dic2 and key1 not in union:
                    union.extend([key1] * dic1[key1])
                if key2 not in dic1 and key2 not in union:
                    union.extend([key2] * dic2[key2])
    
    if len(intersection) == 0:
        return 0
    
    answer = int((len(intersection) / len(union)) * 65536)                    
            
    return answer