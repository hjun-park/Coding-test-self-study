def binary_search_iterable(array, target, start, end):
    # 01. 제약조건 : 시작점이 끝점을 넘어서기까지 수행
    while start <= end:
        mid = (start + end) // 2

        # 02-1. 중간점 == 내가 찾는 값
        if array[mid] == target:
            return mid

        # 02-2. 중간점 > 내가 찾는 값  :: 중간점보다 더 작은 쪽을 짚기
        elif array[mid] > target:
            end = mid - 1

        # 02-3. 중간점 < 내가 찾는 값 :: 중간점보다 더 큰 쪽을 짚기
        else:
            start = mid + 1

    return None # 없는 경우


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 결과 출력


