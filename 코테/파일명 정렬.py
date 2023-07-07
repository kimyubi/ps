def solution(files):
    tmp, answer = [], []
    
    for idx, file in enumerate(files):
        head, number, tail = [], [], []
        num_start = False
        
        for x in file:
            if x.isdigit() and not tail:
                if len(number) < 5:
                    num_start = True
                    number.append(x)
                else:
                    tail.append(x)
                continue
                
            if not num_start:
                head.append(x)
                continue
            
            tail.append(x)
            
        tmp.append([idx, ''.join(head).lower(), ''.join(number), ''.join(tail)])
        answer.append([idx, ''.join(head), ''.join(number), ''.join(tail)])
        
    tmp.sort(key= lambda x: (x[1], int(x[2])))
    return [''.join(answer[i][1:]) for i in [item [0] for item in tmp]]