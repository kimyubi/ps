from itertools import product
def solution(users, emoticons):
    answer = []
    n = len(emoticons)
    
    for discount_rate in product([10,20,30,40], repeat = n):
        # 할인율에 따른 이모티콘 구매 비용
        cost = 0
        # 할인율에 따른 이모티콘 플러스 구독자 수 
        subscribe = 0
        
        for user in users:    
            # user_rate 이상의 할인이 있는 이모티콘을 모두 구매한다.
            user_rate, user_price = map(int, user)
            
            emoticon_total = 0
            for i, emoticon_price in enumerate(emoticons):
                if user_rate <= discount_rate[i]:
                    discount_price = int(emoticon_price  *  discount_rate[i] / 100)
                    emoticon_total += emoticon_price - discount_price
                    
            if user_price <= emoticon_total:
                subscribe += 1
            else:
                cost += emoticon_total
                
        answer.append([subscribe, cost])

    answer.sort(key = lambda x: (-x[0], -x[1]))
    
    return answer[0]