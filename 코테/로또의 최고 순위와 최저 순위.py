def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    
    rank = [6,6,5,4,3,2,1]
    
    # 0을 제외한 다른 숫자들은 2개 이상 담겨있지 않기 때문에 set을 사용
    lottos, win_nums = set(lottos), set(win_nums)
    lottos.discard(0)
    
    # 0을 제외했을 때, 일치하는 숫자의 개수
    win_num_cnt = len(lottos) - len(lottos - win_nums)
    
    # 가장 많이 맞힌 경우 
    high = rank[win_num_cnt + zero_cnt] 
    
    # 가장 적게 맞힌 경우
    low = rank[win_num_cnt] 
    
    return [high, low]