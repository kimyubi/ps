# s를 n개 단위로 압축하는 메서드
def compression(s, n):
    tmp = []
    
    # 문자열 s를 n개 단위로 자른다.
    for i in range(0, len(s), n):
        tmp.append(s[i: i+n])
    
    # n개 단위로 자른 문자열을 arr 리스트에 기록한다.
    arr = []
    
    for idx, item in enumerate(tmp):
        next = idx + 1
        
        while next < len(tmp) and tmp[next] == item:
            next += 1

        if idx + 1 < next:
            arr.append(str(next - idx) + item)
            del tmp [idx:next-1]
            
        else:
            arr.append(item)
            
    return len(''.join(arr))
            
    
def solution(s):
    # 문자열 s의 최대 길이가 1000이므로, max 값을 1001로 잡는다.
    answer = 1001
    
    # 문자열의 길이
    n = len(s)
    
    # 문자열을 1개 ~ (문자열의 길이)개 단위로 잘라 압축하여 표현한다.
    for i in range(1, n + 1):
        result = compression(s, i)
        answer = min(result, answer)
        
    return answer