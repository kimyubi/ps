# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
    input = []
    for x in S.split('<'):
        input.append(x)
        
    ans =  len(max(input))
    
    if "<" not in max(input) and ">" not in max(input):
        if ans % 2 != 0:
            print(ans -1)
        else:
            print(ans)

    else:
        if ans % 2 == 0:
            print (ans)
        else:
            print(ans + 1)
        
        

solution("<<?")
solution("???????????")
