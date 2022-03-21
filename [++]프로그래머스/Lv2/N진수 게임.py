import sys

input = sys.stdin.readline


# 10진법 -> N진법 변환 함수
def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    '''
        [아래 예시]
        21을 16진수로 변경하기 위해서는,
        
        1) 21을 진법수 16으로 나눈다. (몫 4, 나머지 1)
         -> 나머지는 결과값에 붙인다.  (결과값 : 1)
        2) (1)과정에서 나온 몫 4를 진법수 16으로 나눈다. (몫 0, 나머지 4)
         -> 나머지는 결과값에 이어붙인다. ( 결과값 : 14 )
        3) 몫은 0이기 때문에 종료하고 결과값이 진법 변환 결과이다.
    '''
    if q == 0:  # 재귀 종료조건
        return temp[r]
    else:
        # 챔퍼나운 수 (진법 수로 나눴을 때 몫은 또 다시 진법으로 나누고, 나머지만 덧붙여준다.)
        return convert(q, base) + temp[r]


# 진법 / 미리 구할 숫자 / 참가인원 / 순서
def solution(n, t, m, p):
    answer = ''
    number = ''

    # 1) 0부터 목표 수까지 N진법에 해당하는 리스트를 만든다.
    #  -> 목표하는 수는 참가인원 * 미리 구할 숫자
    for i in range(t * m):
        number += str(convert(i, n))  # 변환할 숫자 i와 변환할 진법 n

    # 2) 리스트 길이가 t보다 작을 때까지 변환된 리스트에서 튜브가 저장할 단어만 가져온다.
    #  -> 튜브의 순서는 p += m 이다.
    while len(answer) < t:
        answer += number[p - 1]
        p += m

    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
