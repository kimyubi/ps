def solution(sizes):
    tmp = []
    for size in sizes: 
        tmp.append(sorted(size))
    
    size_w, size_y = [list(x) for x in zip(*tmp)]
    
    return max(size_w) * max(size_y)