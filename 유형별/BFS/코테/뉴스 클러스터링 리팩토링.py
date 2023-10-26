def solution(str1, str2):
    answer = 0
    str1 = [str1[i:i+2].lower() for i in range(len(str1) - 2 + 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2) - 2 + 1) if str2[i:i+2].isalpha()]
    
    if not str1 and not str2:
        return 65536
    
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)
    
    gyo_sum = sum([min(str1.count(g), str2.count(g)) for g in gyo])
    hap_sum = sum([max(str1.count(h), str2.count(h)) for h in hap])

    return int((gyo_sum / hap_sum) * 65536)
    
