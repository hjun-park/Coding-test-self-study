'''
0. defaultdict(list) 사용
1. info 순회하며 딕셔너리 저장 (key: 문자열, value: 점수리스트(int))
 - 각 파트별로 '-' 하이픈 넣어서도 저장한다.
2. 딕셔너리 순회하며 value 오름차순 정렬
3. query 파싱
4. query 문자열을 key로 해서 가져온 value 이분탐색

query



'''

from bisect import bisect_left  # lower bound
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []

    # 0. defaultdict(list) 사용
    _dict = defaultdict(list)

    # 1. info 순회하며 딕셔너리 저장 (key: 문자열, value: 점수리스트(int))
    for o in info:
        row = o.split()
        info_key = row[:-1]  # 나머지 정보
        info_value = row[-1]  # score

        # 0개부터 4개까지 선택하는 경우의 수
        for select in range(0, 5):
            for com in list(combinations(info_key, select)):
                _dict[''.join(com)].append(int(info_value))

    # 2. 딕셔너리 순회하며 value 오름차순 정렬
    for key in _dict.keys():
        _dict[key].sort()

    # 3. query 파싱
    for q in query:
        row = [x for x in q.split() if x != 'and' and x != '-']
        query_key = row[:-1]
        query_value = row[-1]

        # 4. query 문자열을 key로 해서 가져온 value 이분탐색
        target = _dict[''.join(query_key)]
        idx = bisect_left(target, int(query_value))
        cnt = len(target) - idx
        answer.append(cnt)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
