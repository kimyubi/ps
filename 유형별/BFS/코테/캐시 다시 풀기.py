def solution(cacheSize, cities):
    dic = dict()
    cities = [city.lower() for city in cities]
    answer, cache = 0, []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for idx, city in enumerate(cities):
        
        # 캐시 miss
        if city not in cache:
            answer += 5
            
            # 캐시 교체
            if len(cache) + 1 > cacheSize:
                candidate = sorted(dic.items(), key=lambda x: x[1])
                if len(candidate) != 0:
                    for k, v in candidate:
                        if k in cache:
                            cache.remove(k)
                            del dic[k]
                            break
            
            cache.append(city)
                
        # 캐시 hit  
        else:
            answer += 1
        
        # 캐시 참조 시간 갱신
        dic[city] = idx
    
    return answer
    