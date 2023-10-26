def solution(records):
    answer, dic = [], {}
    enter, leave = "님이 들어왔습니다.", "님이 나갔습니다."
    
    for record in records:
        r = record.split()
        
        if r[0] == 'Enter':
            answer.append([r[1], enter])
            dic[r[1]] = r[2]
            
        elif r[0] == 'Leave':
            answer.append([r[1], leave])
        
        else:
            dic[r[1]] = r[2]
    
    return [dic[x[0]] + x[1] for x in answer]