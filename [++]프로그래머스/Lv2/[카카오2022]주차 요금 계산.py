'''
 - fees = [기본시간, 기본요금, 단위시간, 단위요금]
 - records = [(시각 차량번호 내역) ...]

 - 입차는 존재, 출차 없다면 23:59에 처리
 - 시간 : ceil(전체시간 - 기본시간(180) / 10)
 - 차량번호가 작은 자동차부터 배열에 담기

'''

from collections import defaultdict
from datetime import datetime
from math import ceil


def charge_fee(time_dict, fees):
    b_time, b_price, e_time, e_price = fees

    result = []
    for num, parking_time in time_dict.items():
        # 시간 : ceil(전체시간 - 기본시간(180) / 10)
        left_time = ceil((parking_time - b_time) / e_time)

        if left_time > 0:
            pay = b_price + (left_time * e_price)
        else:
            pay = b_price

        result.append([num, pay])

    return [x[1] for x in sorted(result, key=lambda x: x[0])]


def calc_time(_in, _out):
    # 전체시간 계산
    start = datetime.strptime(_in, "%H:%M")
    end = datetime.strptime(_out, "%H:%M")

    diff = end - start
    return diff.seconds // 60  # 분 계산


def solution(fees, records):
    records_dict = defaultdict(str)  # 주차 정보
    time_dict = defaultdict(int)  # 시간 정보

    # 내역 돌면서 시간 카운팅 진행
    for record in records:
        t, num, cmd = record.split()

        if cmd == 'IN':
            records_dict[num] = t

        elif cmd == 'OUT':
            _in = records_dict.pop(num)
            time_dict[num] += calc_time(_in, t)

    # 다 돌고 records_dict에 남아 있는 차량 23:59로 출차 처리
    for key in records_dict.keys():
        _in = records_dict[key]
        time_dict[key] += calc_time(_in, '23:59')

    # 주차요금 계산
    return charge_fee(time_dict, fees)


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
