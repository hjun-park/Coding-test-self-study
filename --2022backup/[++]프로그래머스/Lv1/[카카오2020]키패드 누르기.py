def solution(numbers, hand):
    answer = ''

    # 키패드 좌표료 변경
    pos_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    # 시작 위치
    L_pos = pos_dict['*']
    R_pos = pos_dict['#']

    for n in numbers:
        now = pos_dict[n]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if n in [1, 4, 7]:
            answer += 'L'
            L_pos = now

        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif n in [3, 6, 9]:
            answer += 'R'
            R_pos = now

        # 2, 5, 8, 0을 누르는 경우
        else:
            L_dist = 0
            R_dist = 0

            # 좌표 거리 계산해주기
            for a, b, c in zip(L_pos, R_pos, now):
                L_dist += abs(a - c)
                R_dist += abs(b - c)

            # 왼손이 더 가까운 경우
            if L_dist < R_dist:
                answer += 'L'
                L_pos = now

            # 오른손이 더 가까운 경우
            elif L_dist > R_dist:
                answer += 'R'
                R_pos = now

            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    L_pos = now

                # 오른손잡이 경우
                else:
                    answer += 'R'
                    R_pos = now

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
