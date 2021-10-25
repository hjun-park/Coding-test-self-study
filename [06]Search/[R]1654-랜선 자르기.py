import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in array:
            count += i//mid

        if count >= target:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

# K는 기존 보유, N개는 필요 개수
K, N = map(int, input().split())
lan = []

for _ in range(K):
    lan.append(int(input()))

start, end = 1, max(lan)    # zero division 에러
binary_search(lan, N, start, end)

