import sys

input = sys.stdin.readline

num_dict = [("zero", '0'), ("one", '1'), ("two", '2'), ("three", '3'), ("four", '4'),
            ("five", '5'), ("six", '6'), ("seven", '7'), ("eight", '8'), ("nine", '9')]


def solution(s):
    for num in num_dict:
        s = s.replace(num[0], num[1])

    return int(s)


print(solution("one4seveneight"))
