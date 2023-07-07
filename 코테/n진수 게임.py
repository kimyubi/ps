def solution(n, t, m, p):
    answer = ''
    tmp = ''
    
    for i in range(m * t):
        tmp += convert_notation(i, n)
    
    idx = p - 1
    while len(answer) < t:
        answer += tmp[idx]
        idx += m
    
    return answer


def convert_notation(number, base):
    T = "0123456789ABCDEF"
    q, r = divmod(number, base)

    return convert_notation(q, base) + T[r] if q else T[r]

