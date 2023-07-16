import math
def solution(enroll, referral, seller, amount):
    # dic[판매원 이름 x] : x를 추천한 사람
    info = dict()
    profit = dict()
    
    for e, r in zip(enroll, referral):
        info[e] = r
        profit[e] = 0
    
    
    # 10% 를 계산할 때에는 원 단위에서 절사하며, 
    # 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.
    for s, a in zip(seller, amount):
        a *= 100
        
        remain_amount = math.trunc(a * 10 / 100)
        
        if remain_amount < 1:
            profit[s] += a
            remain_amount = 0
        else:
            profit[s] += a - remain_amount    
        recommender = info[s]
        
        while True:
            if remain_amount == 0 or recommender not in info:
                break
            total_amount = remain_amount
            remain_amount = math.trunc(total_amount * 10 / 100)
            
            if remain_amount < 1:
                profit[recommender] += total_amount
                remain_amount = 0
            else:
                profit[recommender] += total_amount - remain_amount
                
            recommender = info[recommender]
                
    return list(profit.values())