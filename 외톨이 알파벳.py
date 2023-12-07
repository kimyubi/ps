from collections import Counter
def solution(input_string):
    answer = ''
    
    counter1 = Counter(input_string)
    tmp = [input_string[0]]
    
    for i in range(1, len(input_string)):
        if tmp[-1] != input_string[i]:
            tmp.append(input_string[i])
            
    counter2 = Counter(tmp)
    for key in counter1:
        # 2회 이상 나타났는지 check!
        if 2 <= counter1[key]:
            # 2개 이상의 부분으로 나뉘어져있는지 체크
            if key in counter2 and 2 <= counter2[key]:
                answer += key
                
    if not answer:
        return "N"
    
    return ''.join(sorted(list(answer)))