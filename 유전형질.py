def solution(queries):
    answer = []
    def get_genes(generation, idx):
        # 재귀 종료 조건
        if generation == 1:
            return "Rr"
        
        # 부모의 형질을 알아낸다.
        parent = get_genes(generation-1, idx // 4)
        
        if parent == "RR":
            return "RR"
        elif parent == "rr":
            return "rr"
        else:
            which_child = idx % 4
            if which_child in (1, 2):
                return "Rr"
            elif which_child == 0:
                return "RR"
            elif which_child  == 3:
                return "rr"

    for generation, idx in queries:
        answer.append(get_genes(generation, idx - 1))
        
    return answer
        
            
    