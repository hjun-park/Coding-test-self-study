array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# len(array) <= 1 체크
# # 맞을 시 빈 리스트 생성해서 반환
# 피벗선정 [0]
# 슬라이싱 [1:]
# left 사이드 리스트 생성 ( pivot 보다 작은 수 )
# right 사이드 리스트 생성 ( pivot 보다 큰 수 )
# 피벗문자열과 함께 합치는 방향으로 재귀 quick sorting


def quick_sort(array):
    if len(array) <= 1:
        empty_list = []
        return empty_list

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
