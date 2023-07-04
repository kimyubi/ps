from collections import deque
def solution(msg):
    answer = []
    dic = dict()
    
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화 한다.
    last = 26
    for i in range(last):
        dic[chr(65 + i)] = i + 1
    
    msg = deque(msg)
    while msg:
        w = msg.popleft()
        
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        tmp = w
        replace_w = w
        
        for idx, s in enumerate(msg):
            tmp += s
            if tmp in dic:
                i = idx
                replace_w = tmp
        
        # w와 replace_w가 같은 경우, 현재 입력과 일치하는 가장 긴 문자열은 w이다.
        if w == replace_w:
            # w의 색인 번호 출력
            answer.append(dic[w])
            last += 1
            
            # 입력에서 처리되지 않은 다음 글자가 남아있다면(msg[0]),w+msg[0]에 해당하는 단어를 사전에 등록한다.
            if msg:
                dic[w + msg[0]] = last
            
        else:
            # w와 replace_w가 다른 경우, 현재 입력과 일치하는 가장 긴 문자열은 replace_w이다.
            # 입력에서 replace_w를 제거한다.
            for _ in range(len(replace_w) - 1):
                w += msg.popleft()
            
            # replace_w의 색인 번호를 출력
            answer.append(dic[w])
            
            #  현재 입력과 일치하는 가장 긴 문자열 replace_w보다 1만큼 긴 문자열을 사전에 추가한다.
            last += 1
            if msg:
                dic[w + msg[0]] = last

    return answer