def solution(s):
    answer = 0
    alpha_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", 
                "four": "4", "five": "5", "six": "6", "seven": "7", 
                 "eight": "8", "nine": "9"}
    
    for alpha in alpha_dic.keys():
        if alpha in s:
            s = s.replace(alpha, alpha_dic[alpha])
    
    answer = int(s)
        
    return answer