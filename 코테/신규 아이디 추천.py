def solution(new_id):
    not_allowed_character = '~!@#$%^&*()=+[{]}:?,<>/'
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for c in not_allowed_character:
        new_id = new_id.replace(c, '')

    # 3단계
    new_id = list(new_id)
    for idx, x in enumerate(new_id):
        if x == '.':
            now = idx
            next = now + 1
            while next < len(new_id) and new_id[next] == '.':
                next += 1
                
            if now + 1 < next:
                del new_id[now+1:next]
    
    new_id = ''.join(new_id)
    
    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = new_id.rstrip('.')
        
    # 7단계
    if len(new_id) <= 2:
        last_c = new_id[-1]
        
        while len(new_id) < 3:
            new_id += last_c
            
    
    return new_id
