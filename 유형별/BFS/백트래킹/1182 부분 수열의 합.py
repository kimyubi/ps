import sys
input = sys.stdin.readline

# 백트래킹 함수
def back_tracking(idx, res):
    global cnt

    if idx >= n:
        return

    res += k[idx]

    if res == s:
        cnt += 1

    back_tracking(idx + 1, res) # 현재 idx 정수를 더한 것
    back_tracking(idx + 1, res - k[idx]) # 현재 idx 정수를 더하지 않은 것(백트래킹)


n, s = map(int, input().split())
k = list(map(int, input().split()))
cnt = 0

back_tracking(0, 0)
print(cnt)