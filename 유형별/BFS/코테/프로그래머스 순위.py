from collections import defaultdict
def solution(n, results):
    
    answer = 0
    # i에게 이긴 사람
    winner = defaultdict(set)
    # i에게 진 사람
    loser = defaultdict(set)
    
    for w, l in results:
        winner[l].add(w)
        loser[w].add(l)
        
    for i in range(1, n+1):
        for w in winner[i]:
            loser[w].update(loser[i])
            
        for l in loser[i]:
            winner[l].update(winner[i])
            
    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            answer += 1
    
    return answer