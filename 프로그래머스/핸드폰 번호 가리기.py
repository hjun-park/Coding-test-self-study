def solution(phone_number):
    answer = list(phone_number)
    l = len(phone_number) - 4

    for i in range(0, l):
        answer[i] = '*'

    return ''.join(answer)
