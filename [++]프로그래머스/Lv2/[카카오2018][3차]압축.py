'''
[문제이해]
 - LZW 압축 참고

[구현함수 파악]
- input: 문자열
- output: 색인번호

[전체 프로세스]
 - LZW 알고리즘 
 1. 영문 대문자 사전 초기화
 2. 문자열 하나씩 뽑으면서 사전에 있는지 확인하며 저장
 3. 만약 사전에 없는 문자열이라면 이미 뽑은 문자열들은 사전번호로 출력하고 (이미뽑은 문자 + 없는 문자) 새로 등록
 4. 다시 2번부터 반복

[프로세스별 수도코드]


[주석옮기기/전역코드먼저]

'''


def solution(msg):
    answer = []
    exists = ''

    # 영문 대문자 사전 초기화
    idx = 27
    _dict = ({chr(x): x - 64 for x in range(ord('A'), ord('Z') + 1)})

    # 문자열 하나씩 뽑으면서 사전에 있는지 확인하며 저장
    msg = list(msg)
    while msg:
        exists += msg.pop(0)

        if exists not in _dict:  # 사전에 없는 문자열
            answer.append(_dict[exists[:len(exists) - 1]])  # 이미 뽑은 문자 사전번호 출력
            _dict[exists] = idx  # 이미 뽑은 문자 + 없는 문자 새로 등록
            idx += 1

            exists = exists[-1]  # 문자 교체
        else:  # 사전에 있는 문자열
            continue

    # 마지막 처리
    if exists in _dict:
        answer.append(_dict[exists])

    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
