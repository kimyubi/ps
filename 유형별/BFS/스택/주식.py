def solution(prices):
    answer = []
    
    while prices:
        price = prices.pop(0)
        n = 0
        
        for p in prices:
            if p >= price:
                n += 1
        answer.append(n)
            
    print(answer)
            
        
        
        
solution([3,2,1,5,2])