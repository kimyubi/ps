from collections import Counter
from bisect import bisect_right
def solution(N, stages):
    answer = []
    
    stages.sort()
    max_value = stages[-1]
    counter = Counter(stages)
    
    # 스테이지에 도달한 플레이어 수 구하기
    stage_info = dict()
    for i in range(1, N + 1):        
        if i == max_value:
            stage_info[i] = [0,0]
        else:
            stage_info[i] = [counter[i], counter[i]]
            
    if max_value in stage_info:
        stage_info[max_value][1] += counter[max_value]
    else:
        stage_info[max_value-1][1] += counter[max_value]
    
    for stage in set(stages[:]):
        if stage not in stage_info:
            stage_info[stage-1][1] += len(stages) - bisect_right(stages, stage)
        else:
            stage_info[stage][1] += len(stages) - bisect_right(stages, stage)
    

    for key, value in stage_info.items():
        if value[1] == 0:
            result = 0
        elif value[0] == 0:
            if max_value in stage_info:
                result = 1
            else:
                result = 0
        else:
            result = value[0] / value[1]
        
        answer.append([key, result])
        
    answer = [item[0] for item in sorted(answer, key=lambda x: (x[1], -x[0]), reverse=True)]
    return answer