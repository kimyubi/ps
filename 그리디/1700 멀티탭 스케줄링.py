import sys
input = sys.stdin.readline

n, k = map(int, input().split())

device = list(map(int, input().split()))
multitap = []

ans = 0
for i in range(k):
    if device[i] in multitap:
        continue
    
    if len(multitap) < n:
        multitap.append(device[i])
    
    else:
        later_use = 0
        is_laterUse = True
        # 사용중인 디바이스 중에서 나중에 사용하는 디바이스가 없는 경우
        for currentUse in multitap:
            if currentUse not in device[i:]:
                multitap.remove(currentUse)
                multitap.append(device[i])
                
                is_laterUse = False
                
                break
            
            else:
                later_use = max(later_use, device[i:].index(currentUse))
            
        if is_laterUse:
            multitap.remove(device[i:][later_use])
            multitap.append(device[i])
            
        ans += 1
        
print(ans)
                
                 
                
        