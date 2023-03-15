# def solution(name):
#     distance = 0
#     distance1 = 0
#     distance2 = 0
#     next = 0
#     answer = 0
#
#     input_list = list(name)
#
#     solution_list = ['A' for _ in range(len(input_list))]
#
#     # 만약 3자리면서 가운데가 A라면 next = 1
#     if input_list[1] == 'A' and len(input_list) == 3:
#         next = 1
#     else:
#         next = len(input_list)-3
#
#     for ch in input_list:
#         distance1 = int(ord('Z')) - int(ord(ch)) + 1
#         distance2 = int(ord(ch)) - int(ord('A'))
#         # print("distance : ", distance1, distance2)
#
#         distance = min(distance1, distance2)
#         answer += distance
#
#     answer += next
#     return answer

# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.

# 모범답안
# alpha 리스트 : 최소값
def solution(name):
    count = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    indexes = []

    current_idx = 0
    n = len(name)
    # 해당 for문은 A로부터 해당 알파벳 거리까지를 dictionary 형식으로 저장하는 형태
    for i in range(len(alpha)):
        d[alpha[i]] = min(i, 26 - i)
    print(d)

    # 거리 인덱스를 추가하는 반복문
    for i in range(n):
        num = d[name[i]]  # 입력받은 각 문자 자리마다 거리를 num에 저장
        count += num  # 총 거리를 구하기 위해 더함
        if num != 0:  # A가 아니라면
            indexes.append(i)  # 인덱스 값 indexes에 추가 (A는 indexes에 추가 X)
    while True:
        if len(indexes) == 0:
            break
        print("indexes", indexes)
        min_dist = 99
        min_idx = 0
        for it in indexes:  # indexes 배열 : A가 아닌 문자의 인덱스를 저장하고 있음 ( ex) JAN 입력 받으면 J와 N의 인덱스인 [0, 2] 저장
            # 현재 자리(최초 0) 위치에서 해당 인덱스까지 앞으로 혹은 뒤로 가는게 빠를 지 확인
            min_dist2 = min(abs(it - current_idx), n - abs(it - current_idx))
            if min_dist2 < min_dist:
                min_dist = min_dist2
                min_idx = it  # 이동한 인덱스 저장
        count += min_dist  # 해당자리 이동거리 추가
        indexes.remove(min_idx)  # 설정했으니 인덱스 제거
        current_idx = min_idx  # 이동했으니 이동한 자리 인덱스로 교체

    return count


if __name__ == '__main__':
    count = solution("JAZ")
    print(solution("BBBAAAB"))  # 9
    print(solution("ABABAAAAABA"))  # 11
    print(solution("CANAAAAANAN"))  # 49
    print(solution("ABAAAAABAB"))  # 8
    print(solution("ABABAAAAAB"))  # 10
    print(solution("BABAAAAB"))  # 7
    print(solution("AAA"))  # 0
    print(solution("ABAAAAAAABA"))  # 6
    print(solution("AAB"))  # 2
    print(solution("AABAAAAAAABBB"))  # 12
    print(solution("ZZZ"))  # 5
    print(solution("BBBBAAAAAB"))  # 12
    print(solution("BBBBAAAABA"))  # 13
