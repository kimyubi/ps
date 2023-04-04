from itertools import permutations

def play(k,inputs):
    answer = 0
    for min_require, use_power in inputs:
        if k < min_require:
            return answer
        
        k -= use_power
        answer += 1
    
    return answer
    

def solution(k, dungeons):
    answer = -1
    for x in permutations(dungeons , len(dungeons)):
        answer = max(answer, play(k,x))
    
    return answer