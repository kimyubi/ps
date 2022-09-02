
def solution(s):
    sum = 0
    
    for i in range(len(s)):
        if i == 0:
            sum += int(s[i])
            
        else:
            if int(s[i-1]) <= 1 or int(s[i]) <= 1:
                sum += int(s[i])
            else:
                sum *= int(s[i])
    
    return sum
                
            
    
print(solution('567'))
        
        