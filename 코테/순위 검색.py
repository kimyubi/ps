def solution(info, query):
    answer = []
    for q in query:
        q = q.replace('and', ' ').split()
        lang, group, career, food, score = map(str, q)
        score = int(score)
        cnt = 0
        
        for i in info:
            ilang, igroup, icareer, ifood, iscore = map(str, i.split())
            iscore = int(iscore)
            if lang != '-' and ilang != lang:
                continue
            elif group != '-' and igroup != group:
                continue
            elif career != '-' and icareer != career:
                continue
            elif food != '-' and ifood != food:
                continue
            elif iscore < score:
                continue
            
            cnt += 1
        answer.append(cnt)
            
    return answer
    