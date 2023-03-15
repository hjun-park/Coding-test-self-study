import sys


def binary_search(array, target, start, end):  # 가게부품리스트, 찾고자 하는 값, 시작, 끝
    while start <= end:  # start가 end 초과 시 종료
        mid = (start + end) // 2

        # 중간값이 찾으려는 값이면 반환
        if array[mid] == target:
            return mid

        # 중간값이 찾고자 하는 값보다 작으면 mid 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1

        # 중간값이 찾고자 하는 값보다 크면 mid 오른쪽 확인
        else:
            start = mid + 1

    return None


if __name__ == '__main__':

    '''
        # 입력 파트 #
    '''
    n = int(input())  # 가게 부품 개수
    array = list(map(int, input().split()))  # 가게에 있는 전체 부품 번호
    array.sort()  # 이진탐색 위해 정렬 수행

    m = int(input())  # 손님이 탐색 요청한 개수
    x = list(map(int, input().split()))  # 손님이 확인 요청한 전체 부품 번호 공백 구분 입력

    '''
        # 로직 #
    '''
    for i in x:  # 손님이 탐색 요청한 부품 번호 하나씩 확인
        result = binary_search(array, i, 0, n - 1)

        if result is not None:
            print('yes', end=' ')
        else:
            print('no', end=' ')
