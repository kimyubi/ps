import sys

input = sys.stdin.readline

# 집의 개수 n, 공유기의 개수 c
n, c = map(int, input().split())

# 집의 좌표를 나타내는 리스트 housess
houses = sorted([int(input()) for _ in range(n)])

ans = 0
def solution(start, end):
    global ans
    while start <= end:
        mid = (start + end) //  2
        
        standard = houses[0]
        cnt = 1
        
        for i in range(1, n):
            if houses[i] - standard >= mid:
                cnt += 1
                standard = houses[i]

        # mid를 늘려야 함
        if cnt >= c:
            start = mid + 1
            ans = mid
             
        else:
            end = mid - 1
        
        

            
solution(1, houses[n-1] - houses[0])
print(ans)
