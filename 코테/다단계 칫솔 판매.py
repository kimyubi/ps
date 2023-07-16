def solution(enroll, referral, seller, amount):
    # info[판매원 이름 x] : x를 추천한 사람
    # profit[판매원 이름 x] : x의 수익
    
    info, profit = dict(), dict()
    
    for e, r in zip(enroll, referral):
        info[e] = r
        profit[e] = 0
    
    for s, a in zip(seller, amount):
        a *= 100

        remain_amount = int(a * 10 / 100)
        
        if remain_amount < 1:
            profit[s] += a
            remain_amount = 0
        else:
            profit[s] += a - remain_amount    
            
        recommender = info[s]
        
        while True:
            if remain_amount == 0 or recommender not in info:
                break
            
            # 10% 를 계산할 때에는 원 단위에서 절사하며, 
            # 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.
            total_amount = remain_amount
            remain_amount = int(total_amount * 10 / 100)
            
            if remain_amount < 1:
                profit[recommender] += total_amount
                remain_amount = 0
            else:
                profit[recommender] += total_amount - remain_amount
                
            recommender = info[recommender]
                
    return list(profit.values())