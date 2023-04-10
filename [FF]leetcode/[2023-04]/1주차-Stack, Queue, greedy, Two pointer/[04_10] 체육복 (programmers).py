def solution(n, lost, reserve):
    # 1) 자신이 여벌 체육복을 갖고 왔는데 자신 체육복을 잃어버린 경우는
    # 사실상 자기가 입어야하기 때문에 사실상 체육복을 빌려줄 수 없다.

    # 차집합을 이용하여 여벌 체육복을 갖고 왔는데 체육복을 잃어버린 경우는 제외한다.
    # 이 방법은 테스트케이스가 추가된 현재 (23/04/10) 되지 않는다.
    # _lost = [l for l in lost if l not in reserve]
    # _reserve = [r for r in reserve if r not in lost]

    # set을 이용한 방식
    # # 1. 중복을 제거한다.
    # # 2. A - B를 진행한다. ( A - B = ( A - A U B ) ) -> A에서 B를 걸러서 나온다.
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    # 2. 여벌 옷을 순회하면서 앞뒤 확인 후 체육복 없는 학생에게 빌려준다.
    # 앞 먼저 확인 후 뒤를 확인한다.
    for r in _reserve:
        # 1. 앞 뒤 설정
        front = r - 1
        back = r + 1

        # 2. front 먼저 _lost에 있는지 확인
        if front in _lost:
            _lost.remove(front)
        # 3. 다음 back 확인
        elif back in _lost:
            _lost.remove(back)

    # 3. 전체 인원 - 잃어 버린 학생
    return n - len(_lost)


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(2, [2], [2]))  # 2
