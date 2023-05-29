# 문자열 U가 올바른 괄호 문자열인지 확인한다.
def is_correct(u):
    stack = []
        
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if not len(stack):
                return False
            elif stack[-1] == '(':
                stack.pop()
        
    return False if len(stack) else True
    
    
# 문자열 두 균형잡힌 괄호 문자열 u, v로 분리한다.
def separateUV(p):
    left, right = 0, 0
    for idx, x in enumerate(p):
        if x == '(':
            left += 1
        else:
            right += 1
            
        if left == right:
            u, v = p[:idx + 1], p[idx + 1 :] if idx + 1 < len(p) else ''
            break
    return u, v
        
def recursion(p):
    result = ''
    if p == '':
        return ''
        
    u, v = separateUV(p)
        
    # u가 올바른 괄호 문자열이라면
    if is_correct(u):
        result = u + recursion(v)
            
    else:
        tmp = "("
        tmp += recursion(v)
        tmp += ")"
            
        u = u[1:-1]
            
        for c in u:
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
                    
        result += tmp
    return result

def solution(p):     
    if len(p) == 0:
        return ""
    
    return recursion(p)