import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
comp_numbers = list(map(int, input().split()))

# for comp in comp_numbers:
#     if comp in numbers:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

for comp in comp_numbers:
    result = binary_search(numbers, comp, 0, N - 1)
    print(result, end=' ')
