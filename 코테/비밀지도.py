def solution(n, arr1, arr2):
    answer = []
    
    arr1 = [str(bin(number))[2:].zfill(n).replace('1','#').replace('0', ' ') for number in arr1]
    arr2 = [str(bin(number))[2:].zfill(n).replace('1','#').replace('0', ' ') for number in arr2]
    
    for row in range(n):
        tmp = ""
        
        # 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.
        for s1, s2 in zip(arr1[row], arr2[row]):
            if s1 == "#" or s2 == "#":
                tmp += "#"
                continue
            # 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
            if s2 == ' ' and s2 == ' ':
                tmp += ' '
                continue
                
        answer.append(tmp)
        
    return answer