import sys, os


def fear(n, pp):
    result = 0  # total group
    count = 0  # the people per group

    # 2. Looping
    for i in pp:  # 공포도가 낮은 것부터 확인
        count += 1  # 한 그룹 포함되는 인원 +1
        if count >= i:  # 공포도보다 모험가 수가 더 많다면
            result += 1  # 그룹 결성
            count = 0  # 인원추가 되었으니 그룹에 있는 모험가 수 초기화

    return result


if __name__ == '__main__':
    N = sys.stdin.readline().rstrip()
    people = list(map(int, input().split()))

    # 1. Sorting
    people.sort()

    print(fear(N, people))



