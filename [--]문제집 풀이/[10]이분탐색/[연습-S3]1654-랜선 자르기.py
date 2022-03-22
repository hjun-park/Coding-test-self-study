import sys

input = sys.stdin.readline

K, N = map(int, input().split())  # 랜선 개수, 필요한 랜선
lans = [int(input().rstrip()) for _ in range(K)]

max_lan = -1


def binary_search(start, end):
    global max_lan
    while start <= end:
        cnt = 0  # 자른 랜선의 갯수
        mid = (start + end) // 2

        for l in lans:  # 랜선의 개수 체크
            cnt += (l // mid)

        # cnt가 필요한 랜선 N을 넘으면 값을 반영
        if cnt >= N:
            max_lan = max(max_lan, mid)
            start = mid + 1

        # 자른 랜선 개수가 적은 경우 ( 자른 랜선의 길이가 긴 경우 )
        else:
            end = mid - 1


binary_search(1, max(lans))
print(max_lan)
