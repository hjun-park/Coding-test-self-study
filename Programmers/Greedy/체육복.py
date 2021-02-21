# n : 전체 학생
# lost : 체육복 도난 당한 학생 배열
# reserve : 여벌옷 가져온 학생 리스트
def my_solution(n, lost, reserve):
    answer1 = 0
    pe_list = [1 for _ in range(0, n)]

    for i in lost:
        pe_list[i - 1] -= 1

    for j in reserve:
        pe_list[j - 1] += 1

    for k in range(len(pe_list)):
        if pe_list[k] > 1:
            if k > 0 and pe_list[k - 1] == 0:
                pe_list[k] -= 1
                pe_list[k - 1] += 1
                continue
            elif k < len(pe_list) - 1 and pe_list[k + 1] == 0:
                pe_list[k] -= 1
                pe_list[k + 1] += 1
                continue

    for i in range(len(pe_list)):
        if pe_list[i] > 0:
            answer1 += 1

    return answer1


'''
 다른 사람의 풀이
'''


def other_solution(n, lost, reserve):
    # 1. 차집합을 이용해서 풀었음
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    # 2. 체육복 여벌 옷이 있는 사람의 앞 뒤 ( f, b ) 를 지정
    #     여벌 옷 있는 사람의 앞을 먼저 보고 빼는데 그 사람이 체육복을 가지고 있다면,
    #     뒤에 사람이 체육복 가지고 있는지 확인해보고 뺀다. 앞뒤로 가지고 있다면 체육복을 가지고 있는게 아니니까 remove를 하지 않음
    #     그렇게 해서 전체 체육복 가지고 있는 사람 - 제거되지 않은 lost 수를 빼면 answer 출력
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    answer2 = n - len(_lost)

    return answer2


if __name__ == '__main__':
    lost = [2, 4]
    reserve = [3]
    n = 5
    answer1 = my_solution(n, lost, reserve)
    answer2 = other_solution(n, lost, reserve)

    print("return : ", answer1)
    print("return : ", answer2)
