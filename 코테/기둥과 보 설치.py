def possible(answer):
    for x, y, type in answer:
        # 기둥
        if type == 0:
            if y == 0 or (x-1, y, 1) in answer or (x, y, 1) in answer or (x, y-1, 0) in answer:
                continue
            return False
        else:
            if ((x-1, y, 1) in answer and (x+1, y, 1) in answer) or (x, y-1, 0) in answer or (x+1, y-1, 0) in answer:
                continue
            return False
    return True
        
            

def solution(n, build_frame):
    answer = set()
    
    for x, y, type, build in build_frame:
        item = (x, y, type)
        
        if build:
            answer.add((x, y, type))
            
            if not possible(answer):
                answer.remove(item)
        else:
            answer.remove(item)
            if not possible(answer):
                answer.add(item)
                
        
    return sorted(list(answer), key = lambda x : (x[0], x[1], x[2]))