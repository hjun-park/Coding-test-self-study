'''
    min heap sort
'''

# 최소 힙 정렬(오른차순 힙 정렬)

import heapq


def min_heapq_sort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = min_heapq_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

'''
    max heap sort
'''


# 최대 힙 정렬


def max_heapq_sort(iterable):
    r = []
    result = []

    for value in iterable:
        heapq.heappush(r, -value)

    for _ in range(len(r)):
        result.append(-heapq.heappop(r))

    return result


result = max_heapq_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
