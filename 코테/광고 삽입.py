n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
print(arr)def time_to_second(time):
    start, end = time.split("-")
    
    # 시작 시간을 초 단위로 변환한다.
    s = start.split(":")
    start = int(s[0]) * 60 * 60 + int(s[1]) * 60 + int(s[2])
    # 종료 시간을 초 단위로 변환한다.
    e =  end.split(":")
    end = int(e[0]) * 60 * 60 + int(e[1]) * 60 + int(e[2])
    
    return [start, end]

def second_to_time(time):
    h = time // 3600
    h = str(h).zfill(2)
    
    time %= 3600
    
    m = time // 60
    m = str(m).zfill(2)
    
    time = time % 60
    s = str(time).zfill(2)

    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    standard = '00:00:00'
    
    # 동영상 재생시간과 광고 재생시간이 같으면, 삽입할 수 있는 위치는 00:00:00이 유일하다.
    if play_time == adv_time:
        return standard
    
    play_time = standard + '-' + play_time
    play_start, play_end = time_to_second(play_time)
    
    adv_time = standard + '-' + adv_time
    adv_start, adv_end = time_to_second(adv_time)
    adv_time = adv_end - adv_start
    
    time_table = [0] * (play_end - play_start + 1)
    n = len(time_table)
    
    for log in logs:
        start, end = time_to_second(log)
        time_table[start] += 1
        time_table[end] += -1
        
    # 구간별 누적 시청자 수 계산
    for i in range(1, n):
        time_table[i] += time_table[i-1]
        
    # 구간별 최대 누적 시청자 수를 구하기 위해 누적합 계산
    for i in range(1, n):
        time_table[i] += time_table[i-1]
    
    max_view, max_view_time = 0, 0
    for i in range(adv_time -1, n):
        if i < adv_time:
            if max_view < time_table[i]:
                max_view = time_table[i]
                max_time = i - adv_time + 1
        else:
            if max_view < time_table[i] - time_table[i - adv_time]:
                max_view = time_table[i] - time_table[i - adv_time]
                max_time = i - adv_time + 1
                
    return second_to_time(max_time)