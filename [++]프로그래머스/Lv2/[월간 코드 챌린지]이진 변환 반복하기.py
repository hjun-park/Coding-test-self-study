def solution(s):
    cnt = 0
    turn = 0

    while True:
        cnt += s.count('0')
        if s == '1':
            break
        next_s = bin(len(s.replace('0', '')))[2:]

        s = next_s
        turn += 1

    return [turn, cnt]
