# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m
# 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착한다.
def convert_to_minute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def convert_to_time(minute):
    h, m = map(str, divmod(minute, 60))
    return h.zfill(2) + ":" + m.zfill(2)

def solution(n, t, m, timetable):
    suttle = dict()
    
    timetable = [convert_to_minute(t) for t in timetable]
    timetable.sort()
    
    # 셔틀 버스가 오는 시간 suttletable
    for i in range(n):
        suttle[540 + t * i] = []
        
    for crew_time in timetable:
        for suttle_time in suttle.keys():
            if crew_time <= suttle_time and len(suttle[suttle_time]) < m:
                suttle[suttle_time].append(crew_time)
                break
    
    answer = 0
    for key, value in suttle.items():
        personnel = len(suttle[key])
        if personnel < m:
            answer = key
        else:
            answer = suttle[key][-1] - 1
    return convert_to_time(answer)