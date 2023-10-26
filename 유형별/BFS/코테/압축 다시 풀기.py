def solution(msg):
    answer = []
    dic = {chr(i+65) : i+1 for i in range(26)}
    
    w = c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c
    return answer