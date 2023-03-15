import sys

input = sys.stdin.readline


# https://velog.io/@eehwan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''
    투포인터를 이용하는 문제
'''
def solution(a):

    result = [False] * len(a)
    left, right = int(1e9), int(1e9)

    # 자신(a[i])의 왼쪽이나 오른쪽에 자기보다 큰 수가 존재하는지 확인
    # 왼쪽이나 오른쪽 한 곳에 큰 수만 존재할 시 마지막까지 남기기 가능

    # 투포인터 이용, 양쪽 끝에서부터 하나하나 left, right보다 작은지 체크하며 갱신한다.
    # 그렇게 해서 작은 값을 찾아 갱신을 시키면 그 수는 살아남을 수 있는 수 이다.
    for i in range(len(a)):
        if a[i] < left:
            print(f'left {a[i]}')
            left = a[i]
            result[i] = True

        if a[-1-i] < right:
            print(f'right {a[-1-i]}')
            right = a[-1-i]
            result[-1-i] = True

    return sum(result)


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
