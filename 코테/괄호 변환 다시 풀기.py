# '('와 ')'의 개수가 같다면 균형잡힌 문자열
# 올바른 괄호 문자열이고 괄호의 짝도 모두 맞을 경우 올바른 괄호 문자열

def separateUV(p):
    left, right = 0, 0
        
    for idx, x in enumerate(p):
        if x == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            u, v = p[:idx + 1], p[idx + 1:] if idx + 1 < len(p) else ''
            break
                
    return u, v
    
def is_correct(p):
    stack = []
        
    for c in p:
        if c == '(':
            stack.append('(')
        else:
            if not len(stack):
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                        
    return True if not len(stack) else False
    
def recursion(p):
    result = ''
        
    if not len(p):
        return ''
        
    u, v = separateUV(p)
        
    if is_correct(u):
        result = u + recursion(v)
    
    else:
        tmp = '('
        tmp += recursion(v)
        tmp += ')'
            
        u = u[1:-1]
            
        for c in u:                
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
            
        result += tmp
        
    return result
            
def solution(p):
    if not len(p):
        return ''
    
    return recursion(p)

