def solution(msg):
    answer = []
    dic = dict()
    last = 26
    for i in range(last):
        dic[chr(65 + i)] = i + 1
    
    point = -1
    for idx, w in enumerate(msg):
        if idx <= point:
            continue
        
        next = idx + 1
        c = msg[idx:next + 1] # KA
        result = ''
        tmp = ''
        if c in dic:
            while True:
                if c in dic:
                    tmp = c
                    next += 1
                    c = msg[idx:next + 1]
                    result = c
                    break
                c = msg[idx:next + 1]
                next += 1
        else:
            answer.append(dic[w])
            last += 1
            dic[c] = last
            continue
            
        answer.append(dic[tmp])
        last += 1
        dic[result] = last
        point = next - 1
            
            
    return answer
        
