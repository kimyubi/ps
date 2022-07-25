while True:
    sentence = input()
    if sentence == ".":
        break
    
    sentence_to_list = []
    stack = []
    sentence = sentence.replace(" ", "")
    flag = False
    
    for s in sentence:
        if s in ("(",")","[","]"):
            sentence_to_list.append(s)
    
    for s in sentence_to_list:
        if s in ("(","["):
            stack.append(s)
            continue
        
        elif not stack:
            stack.append(s)
            break
        
        elif stack[-1] == "(" :
            if s == ")":
                stack.pop()
            else:
                stack.append(s)
        
        elif stack[-1] == "[":
            if s == "]":
                stack.pop()
            else:
                stack.append(s)
            
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
        