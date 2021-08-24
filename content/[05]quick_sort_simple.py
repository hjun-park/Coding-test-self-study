# 간단한 quick sort 버전
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

i = 0
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지고 있다면 정렬 할 필요가 없으므로 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # pivot = 첫 번째 요소
    tail = array[1:]  # pivot을 제외한 나머지

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후 반환
    print(f'======= {i} =======')
    print(left_side)
    print(right_side)
    print(left_side + [pivot] + right_side)

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
