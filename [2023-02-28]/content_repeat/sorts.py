import sys


def binary_search_iter_v2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1


def quick_sort_v2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_v2(left_side) + [pivot] + quick_sort_v2(right_side)


def count_sort_v2(array):
    # 1. 가장 큰 max 사이즈보다 1 큰 배열 생성
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')


# quick sort
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def count_sort(array):
    # 1. 가장 큰 수만큼의 사이즈를 가진 배열
    count = [0] * (max(array) + 1)

    # 2. 배열을 순회하면서 count 배열 값 += 1
    for i in range(len(array)):
        count[array[i]] += 1

    # 3. count 배열 크기만큼 순회
    # 3-1. count 배열 값만큼 순회하면서 출력
    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')


def binary_search_iterable(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 중간값이 찾는 값이라면 중간값을 반환
        if array[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

i = 0

print(quick_sort_v2(array))
print(count_sort_v2(array))
print(binary_search_iter_v2(array, 2, 1, 9))
