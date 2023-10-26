from collections import defaultdict
def solution(genres, plays):
    result = defaultdict(list)
    dic = defaultdict(int)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre] += play
        result[genre].append(list((play, i)))
    
    # 속한 노래가 많이 재생된 장르를 먼저 수록한다.
    dic = sorted(dic, key=lambda x: -dic[x])
 
    answer = []
    
    for x in dic:
        # 장르 내에서 많이 재생된 노래 먼저 수록
        # 재생 횟수가 같으면 고유 번호가 낮은 노래 먼저 수록
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
    
    

    
