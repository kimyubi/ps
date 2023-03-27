def solution(picks, minerals):
    answer = 0
    # dia, iron, stone -> 다이아 곡괭이의 수, 철 곡괭이의 수, 돌 곡괭이의 수
    dia, iron, stone = picks[0], picks[1], picks[2]
    
    # 곡괭이 사용 가능 횟수보다 광물의 수가 더 많으면
    # 곡괭이의 사용 가능 횟수를 초과하는 광물은 캘 수 없다.
    if(sum(picks) * 5 < len(minerals)):
        minerals = minerals[:sum(picks) * 5]
    
    # 광물을 5개 묶음으로 나누기
    chuncs = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    counter = []
    for chunc in chuncs:
        dia_cnt = chunc.count("diamond")
        iron_cnt = chunc.count("iron")
        stone_cnt = chunc.count("stone")
        
        counter.append([dia_cnt, iron_cnt, stone_cnt])
    # 귀한 광물이 더 많이 포함된 청크를 앞에 오도록 정렬한다.
    counter.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    for x in counter:
        # 다이아 곡괭이로 광물을 캐는 경우
        if dia > 0:
            answer += sum(x)
            dia -= 1
            continue
        # 철 곡괭이로 광물을 캐는 경우
        elif iron > 0:
            answer += x[0] * 5 + x[1] + x[2]
            iron -= 1
            continue
        # 돌 곡괭이로 광물을 캐는 경우
        elif stone > 0:
            answer += x[0] * 25 + x[1] * 5 + x[2]   
            stone -=1
            continue
        # 쓸 수 있는 곡괭이가 하나도 없는 경우
        else:
            break
            
    return answer
            
            
            
        
        
        
    
    
            
        