from collections import defaultdict

def solution(genres, plays):
    result = defaultdict(list)
    dic = defaultdict(int)
    
    i = 0
    for genre, play in zip(genres, plays):
        # 속한 노래가 많이 재생된 장르 찾기
        dic[genre] += play
        
        # 장르, 재생 횟수, 고유 번호 기록
        result[genre].append(list((play, i)))
        i += 1 
    
    dic = sorted(dic, key=lambda x: -dic[x])
 
    answer = []
    
    for x in dic:
        # 1. 장르 내에서 많이 재생된 노래 먼저, 고유 번호가 낮은 노래 먼저
        result[x].sort(key=lambda x: (-x[0], x[1]))
        cnt = 1
        for y in result[x]:
            # 장르별로 가장 많이 재생된 노래 두개만 수록
            if cnt <= 2:
                answer.append(y[1])
            else:
                break
            cnt += 1
        
    return answer
    
    

    
