'''
[문제이해/제약조건]
1. 후보키
 - 유일성 : 모든 튜플에 대해 유일하게 하난만 존재하는 컬럼
 - 최소성 : 유일성 만족하는 속성으로 모았을 때 하나라도 빠지면 유일성이 결여되는 경우
2. 후보키의 개수를 구해라

[전체프로세스]
1. combination 이용하여 컬럼을 선택하는 여러 케이스를 구함
2. (1)에서 선택한 케이스를 대상으로 유일성을 만족하는 조합을 찾음
3. (2)에서 나온 결과를 대상으로 최소성을 만족하는 조합을 찾음

[프로세스별 코드]


[주석 옮기기]
'''

from itertools import combinations


def solution(relation):
    answer = 0
    N, M = len(relation), len(relation[0])

    # 0. combinations를 이용하여 케이스를 구함
    candidates = []
    for col in range(1, M + 1):
        candidates.extend(combinations(range(M), col))

    # 1. 유일성을 만족하는 컬럼을 찾음
    # # 학생 테이블에서 각 row의 지정한 컬럼(i)만을 튜플로 tmp에 저장
    # # tmp에는 지정한 특정 컬럼만 들어가게 된다.
    unique = []
    for candi in candidates:
        temp = [tuple([row[i] for i in candi]) for row in relation]

        # 유일성을 만족하는 경우 컬럼 index를 집어넣음
        if len(set(temp)) == N:
            unique.append(candi)

        # 2. 최소성을 만족하는 컬럼 찾음
        # # unique[i]의 길이 == unique[i] & unique[j]
        # # 위의 경우 교집합을 구한 것과 길이가 같다면 unique[i] = {1, 2}, unique[j] = {1, 2, 3} 이런 의미다. 최소성 만족 (X)
        answer = set(unique)
        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                if len(unique[i]) == len(set(unique[i]).intersection(unique[j])):
                    answer.discard(unique[j])

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
