answer = []


def hanoi(n, at, to, aux):
    if n == 1:
        answer.append([at, to])
        return

    # 원반 n-1개를 보조기둥(2번)으로 이동
    hanoi(n - 1, at, aux, to)

    # 가장 큰 원반은 3번 기둥 (목적지)로 이동
    answer.append([at, to])

    # 나머지 보조기둥(2번) -> 목적지(3번) 이동
    hanoi(n - 1, aux, to, at)


def solution(n):
    hanoi(n, 1, 3, 2)
    print(answer)
    return answer


print(solution(2))
