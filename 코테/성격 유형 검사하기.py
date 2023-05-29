def solution(survey, choices):
    answer = ''
    dic = dict()
    
    standard = ['RT', 'CF', 'JM', 'AN']
    for s in standard:
        dic[s[0]] = 0
        dic[s[1]] = 0

    for (disagree, agree), choice in zip(survey, choices):          
        if choice <= 4:
            dic[disagree] += 4 - choice
        
        else:
            dic[agree] += choice - 4
        
    for s in standard:
        a, b = s[0], s[1]
        if dic[a] >= dic[b]:
            answer += a
        else:
            answer += b 
    
    return answer