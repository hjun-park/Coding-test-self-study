'''
[참고] : https://dev-note-97.tistory.com/128
'''

from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    # 1) course 순회
    for k in course:
        can_course = []
        # 2) 주문 순회하며 조합 생성
        for order in orders:
            combi = list(combinations(sorted(order), k))  # 정렬 필수
            # can_course.extend(combi)    # can_course += combi [같은 의미]
            can_course += combi

        # 3) 한 코스 k에 대해 모든 주문을 순회하면, Counter 생성
        cnt_dict = Counter(can_course)

        # 4) 생성된 코스 후보들의 길이가 0이 아니면서 2번 이상 주문됐는지 확인
        if len(cnt_dict) != 0 and max(cnt_dict.values()) >= 2:
            # 5) 가장 많이 주문 된 후보들만 answer에 담기
            answer += [''.join(x) for x in cnt_dict if cnt_dict[x] == max(cnt_dict.values())]

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
