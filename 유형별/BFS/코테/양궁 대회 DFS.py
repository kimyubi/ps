def solution(n, info):
    max_diff = -1
    answer = []
    
    def calculate_score(lion, apeach):
        a, l = 0, 0
        for idx, (l_arrow, a_arrow) in enumerate(zip(lion, apeach)):
            if l_arrow == a_arrow == 0:
                continue
            if l_arrow > a_arrow:
                l += (10 - idx)
            else:
                a += (10 - idx)
        return a, l
    
    
    def dfs(lion, idx):
        nonlocal answer, max_diff, info
        
        # 라이언의 점수판이 완성된 경우
        if idx == 11:
            arrow_used = sum(lion)
            # 라이언이 쏠 수 있는 화살보다 더 많이 쏜 경우 제외
            if n < arrow_used:
                return
            # 라이언이 쏠 수 있는 화살만큼 쏜 경우
            elif n == arrow_used:
                a, l = calculate_score(lion, info)
            # 라이언이 쏠 수 있는 화살보다 덜 쏜 경우 낮은 점수에 화살을 더 쏜다.
            else:
                lion[-1] += (n - arrow_used)
                a, l = calculate_score(lion, info)
            
            
            if a < l:
                if max_diff < l - a:
                    max_diff = l - a
                    answer = [lion[:]]
                    
                elif max_diff == l-a:
                    answer.append(lion[:])
            return
        
        # 어피치보다 화살 1발을 더 쏘는 경우
        lion.append(info[idx] + 1)
        dfs(lion, idx + 1)
        lion.pop()
        
        # 화살 0발을 쏘는 경우
        lion.append(0)
        dfs(lion, idx + 1)
        lion.pop()
        
    dfs([], 0)
    if not answer: return [-1]

    answer.sort()    
    return answer[0]