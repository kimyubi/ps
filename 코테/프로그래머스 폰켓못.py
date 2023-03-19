from collections import Counter
def solution(nums):
    n = len(nums)
    type_cnt = len(Counter(nums).keys())
    
    if n // 2 <= type_cnt:
        return n // 2
    else:
        return type_cnt
    
