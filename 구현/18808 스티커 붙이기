# 노트북의 세로 길이 n, 가로 길이 m, 스티커의 갯수 k
n, m, k = map(int, input().split())

laptop = [[0] * m for _ in range(n)]

# stickers 리스트에 스티커 정보, 행 길이, 열 길이 저장
stickers = []
for i in range(k):
    r, c = map(int, input().split())
    
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append([sticker,r,c])

# 스티커를 시계 방향으로 90도 회전하는 함수
def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    tmp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-1-i] = sticker[i][j]
            
    return tmp
    
# 노트북에 스티커를 붙일 수 있는지 확인하는 함수    
def check(x,y,sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            # 스티커를 붙이려는 자리에 이미 스티커가 붙어있을 때
            if sticker[i][j] == 1 and laptop[x+i][y+j] == 1:
                return False
    
    # 위의 이중 포문이 다 돌때까지 False를 리턴하지 않았다면, 스티커를 붙일 수 있으므로 스티커를 붙인다.
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                laptop[x+i][y+j] = 1
            
    return True
            
    
    
for i in range(k):
    sticker, r, c = stickers[i]
    
    # 스티커를 90도 회전 시키는 횟수
    cnt = 0
    
    while cnt < 4:
        # 스티커가 노트북의 사이즈를 넘을때
        if n < r or m < c:
            r,c,board = c,r,rotate(sticker)
            cnt += 1
            continue
        
        is_attachable = False
        # 스티커의 위치를 조정해도 노트북을 벗어나지 않도록 하는 스티커 시작점의 모든 경우의 수
        for i in range(0,n-r+1):
            for j in range(0,m-c+1):
                if not check(i,j,sticker):
                    continue
        
                else:
                    is_attachable = True
                    break
                    
            
            if is_attachable:
                break
        
        if is_attachable:
            break
        
        else:
            cnt += 1
            r, c, sticker = c, r, rotate(sticker)  
                
    
ans = 0
for row in laptop:
    ans += row.count(1)
    
print(ans)