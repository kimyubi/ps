def solution(money):
    # 집이 하나인 경우 그 집을 터는게 최댓값
    # 집이 두개인 경우 두 집 중 money가 큰 집을 터는게 최댓값
    
    # 첫번째 집을 털고, 마지막 집을 털지 않는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    # 첫번째 집을 털지 않고, 마지막 집을 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money) -1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    

    dp2[len(money)-1] = max(dp2[len(money)-2], dp2[len(money)-3] + money[len(money)-1])
    
    return max(max(dp1), max(dp2))