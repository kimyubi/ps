def solution(brown, yellow):
    sum = brown + yellow
    answer = []
    
    for height in range(1, sum + 1):
        if (sum / height) % 1 == 0:
            width = sum // height
            
            if width >= height:
                if yellow == (width - 2) * (height -2):
                    return [width, height]    
    
    return answer

