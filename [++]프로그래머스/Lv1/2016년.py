import datetime


def solution(a, b):
    day_list = 'MON TUE WED THU FRI SAT SUN'.split()
    return day_list[datetime.datetime(2016, a, b).weekday()]
