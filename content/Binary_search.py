# 재귀함수로 구현한 이진탐색
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우는 왼쪽 재귀 실행
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우는 오른쪽 재귀 실행
    else:
        return binary_search_recursive(array, target, mid + 1, end)


# 반복문으로 구현한 이진탐색
def binary_search_iterable(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1

        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None


# 원소개수 n 찾고자 하는 문자열 target
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 결과 출력
result = binary_search_recursive(array, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)  # 몇 번째 자리


# 01. 원소 개수 n과 찾고자 하는 문자열 target
# 02. array : 전체 원소


