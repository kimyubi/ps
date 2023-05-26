def solution(gems):
    n = len(gems)
    
    # 보석 종류의 수 kind
    kind = len(set(gems))
    answer = [0, n-1]
    start, end = 0, 0
    
    # 보유한 보석의 개수를 나타내는 딕셔너리
    count_dic = {gems[0] : 1, }
    
    while start < n and end < n:
        # 모든 종류의 보석을 포함하고 있지 않은 경우,
        if len(count_dic) < kind:
            end += 1
            if end == n:
                break
            count_dic[gems[end]] = count_dic.get(gems[end], 0) + 1
        
        # 모든 종류의 보석을 포함한 경우, start를 1 증가시킨다.
        else:
            # 현재 구간의 길이가 이전에 저장된 구간의 길이보다 짧은 경우
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
                
            if count_dic[gems[start]] == 1:
                del count_dic[gems[start]]
            else:
                count_dic[gems[start]] -= 1
    
            start += 1
    answer[0] += 1
    answer[1] += 1
        
    return answer