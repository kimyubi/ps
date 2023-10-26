import math
from collections import defaultdict
# 입력 받은 시각 문자열을 분 단위로 변환하여 반환한다.
def time_to_minute(time):
    hour = int(time[0:2])
    minute = int(time[3:])
    
    return hour * 60 + minute

def solution(fees, records):
    answer = []
    
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    default_time, default_cost, unit_time, unit_cost = map(int, fees)

    # 차량 번호를 기준으로 입차 시간과 출차 시간을 기록한다.
    dic_record = defaultdict(list)
    for record in records:
        time, car_num, history = record.split()
        dic_record[car_num].append(time_to_minute(time))
        
    for car_num in dic_record.keys():
        # 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주한다.
        if len(dic_record[car_num]) % 2 != 0:
            dic_record[car_num].append(time_to_minute("23:59"))
            
    # 차량 번호가 작은 순으로 딕셔너리 정렬
    dic_record = sorted(dic_record.items(), key= lambda x: x[0])
   
    for car_num, record in dic_record:
        time = 0
        for i in range(0, len(record) - 1, 2):
            # 주차 시간 누적
            time += record[i+1] - record[i]
        
        # 누적 주차 시간이 기본 시간 이하라면, 기본 요금을 청구한다.
        if time <= default_time:
            answer.append(default_cost)
        
        # 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 
        # 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구한다.
        else:
            additional_cost = math.ceil((time - default_time) / unit_time) * unit_cost
            answer.append(default_cost + additional_cost)
    
    return answer