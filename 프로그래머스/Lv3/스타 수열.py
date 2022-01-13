import sys
from collections import Counter

input = sys.stdin.readline

'''
    참고 링크
    1) [설명] https://inspirit941.tistory.com/316
    2) [코드] https://minhyeok-rithm.tistory.com/entry/%EC%8A%A4%ED%83%80-%EC%88%98%EC%97%B4
'''


def solution(a):
    answer = -1
    if len(a) == 1:
        return 0

    # 1) a 각각의 숫자를 센다.
    n_list = Counter(a)

    '''
        스타수열 최대 가능한 길이는 
        가장 많이 나타난 숫자의 횟수 * 2 (교집합 원소 개수 1개 맞춰야해서 )
    '''
    for key, val in n_list.items():
        # 2) answer는 스타수열 최대길이
        #   만약 value * 2가 answer보다 작으면 패스한다.
        #   구해도 작게 나올텐데 더 구해봤자 연산 낭비이다.
        if val * 2 < answer:
            continue

        i, _len = 0, 0

        # 3) 아닌 경우, a[0]부터 반복문 시작해서 양 옆을 체크(값이 같으면 X)
        #  -> a[i] == a[i+1] 이면 진행하지 않는다. (인접한 값이 같으면 스타배열 X)
        #  -> a[i], a[i+1]이 현재 key와 다르면 진행하지 않는다.
        #    -> 왜냐하면 a[idx]와 a[idx+1] 모두 공통값 k가 없다는걸 의미
        while i < len(a) - 1:

            # 5) (3)에 있는 경우의 수 중 1개만 속하면 인덱스만 증가
            # -> index += 1
            if (a[i] != key and a[i + 1] != key) or a[i] == a[i + 1]:
                i += 1
                continue

            # 4) (3)에 있는 2가지 경우도 아니라면 스타 수열 생성이 가능하다.
            #  -> count += 2 && index += 2
            _len += 2
            i += 2

        answer = max(answer, _len)

    return answer


print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
