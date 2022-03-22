import sys

input = sys.stdin.readline

An, Bn = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


# A에는 속하면서 B에는 속하지 않는 경우

result = []
for a in A:
    if binary_search(B, a, 0, Bn - 1) is None:
        result.append(a)

result = sorted(result)
print(len(result))
if result:
    print(*result)
